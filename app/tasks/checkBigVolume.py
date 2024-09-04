from datetime import datetime
from celery import shared_task
from sqlalchemy.orm import Session
from celery.utils.log import get_task_logger

from app.core.database import engine_db
from app.repositories import SymbolRepository, BigVolumeRepository
from app.tasks.sendTelegram import SendTelegramTasks, UpdateTelegramTasks, telegram_bot_sendtext
from app.tasks.signyal import signyalTasks


celery_log = get_task_logger(__name__)


@shared_task(
    bind=True,
    autoretry_for=(Exception,),
    retry_backoff=True,
    retry_kwargs={"max_retries": 3},
    name="tv_dump:checkBigVolume",
)
def checkBigVolumeTasks(self, id_symbol: str):
    with engine_db.begin() as connection:
        with Session(bind=connection) as db:
            BigVolumeRepo = BigVolumeRepository(db)
            dataBidVolume = BigVolumeRepo.get(id_symbol)

            symbol = SymbolRepository(db).get(id_symbol)
            if symbol is not None:
                if dataBidVolume is None:
                    volume_rasio = symbol.volume / symbol.volume_ma
                    if volume_rasio > 2.2 and symbol.timeframe == 30:
                        BigVolumeRepo.create(
                            {
                                "id": id_symbol,
                                "id_symbol": id_symbol,
                                "created_at": datetime.now(),
                            }
                        )
                        SendTelegramTasks.apply_async(args=[id_symbol])
                else:
                    if dataBidVolume.message_id is not None:
                        UpdateTelegramTasks.apply_async(args=[dataBidVolume.id, dataBidVolume.message_id])

                if symbol.candle_closed and symbol.timeframe == 30:
                    checkBigVolumeOpenClose(db, id_symbol, symbol.symbol)

                signyalTasks.apply_async(args=[symbol.symbol])


def checkBigVolumeOpenClose(db: Session, id_symbol_triger: str, symbol: str):
    BigVolumeRepo = BigVolumeRepository(db)
    dataBidVolume = BigVolumeRepo.get_opened(symbol)
    reposymbol = SymbolRepository(db)
    for item in dataBidVolume:
        symbolcheck = reposymbol.get(item.id)
        if id_symbol_triger != item.id:
            symbolnow = reposymbol.last(symbol, symbolcheck.timeframe)
            if symbolnow.close > symbolcheck.high or symbolnow.close < symbolcheck.low:
                pesan = "{} udah break {} sekarang posisi di {}"
                if symbolnow.close > symbolcheck.high:
                    BigVolumeRepo.update(symbolcheck.id, {"status_close": datetime.now(), "status_break": "high"})
                    telegram_bot_sendtext(pesan.format(symbolnow.symbol, "HIGH", symbolnow.close), None, item.message_id)
                if symbolnow.close < symbolcheck.high:
                    BigVolumeRepo.update(symbolcheck.id, {"status_close": datetime.now(), "status_break": "low"})
                    telegram_bot_sendtext(pesan.format(symbolnow.symbol, "LOW", symbolnow.close), None, item.message_id)
