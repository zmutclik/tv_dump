from datetime import datetime
from celery import shared_task
from sqlalchemy.orm import Session
from celery.utils.log import get_task_logger

from app.core.database import engine_db
from app.repositories import SymbolRepository, BigVolumeRepository, SignyalRepository
from app.tasks.sendTelegram import SendTelegramTasks, UpdateTelegramTasks, telegram_bot_sendtext

import pytz

celery_log = get_task_logger(__name__)


@shared_task(
    bind=True,
    autoretry_for=(Exception,),
    retry_backoff=True,
    retry_kwargs={"max_retries": 3},
    name="tv_dump:Signyal",
)
def signyalTasks(self, symbol: str):
    with engine_db.begin() as connection:
        with Session(bind=connection) as db:
            repoBV = BigVolumeRepository(db)
            repoSY = SymbolRepository(db)
            repoSi = SignyalRepository(db)
            for item in repoBV.get_opened(symbol):
                from_timezone = pytz.timezone("Asia/Jakarta")
                to_timezone = pytz.timezone("UTC")
                dt = from_timezone.localize(item.created_at)
                dt = dt.astimezone(to_timezone)
                symbolbv = repoSY.find_big_volume(item.SYMBOLS.symbol, dt)
                if symbolbv is not None:
                    if repoSi.get(symbolbv.id) is None:
                        repoSi.create(
                            {
                                "id": symbolbv.id,
                                "id_symbol": symbolbv.id,
                                "symbol": symbolbv.symbol,
                                "waktu": datetime.now(),
                                "method": "BUY" if symbolbv.volume_delta < 0 else "SELL",
                                "open": symbolbv.close,
                            }
                        )
