from celery import shared_task
from sqlalchemy.orm import Session
from celery.utils.log import get_task_logger

from app.core.database import engine_db
from app.repositories import SymbolRepository, BigVolumeRepository


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
            symbol = SymbolRepository(db).get(id)
            if symbol is not None:
                volume_rasio = symbol.volume / symbol.volume_ma
                if volume_rasio > 2.2 and symbol.timeframe == 30:
                    BigVolumeRepository(db).create({"id_symbol": id_symbol})
