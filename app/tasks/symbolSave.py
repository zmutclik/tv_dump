from datetime import datetime
from celery import shared_task
from sqlalchemy.orm import Session
from celery.utils.log import get_task_logger

from app.core.database import engine_db
from app.repositories import SymbolRepository

from app.schemas.symbol import SymbolDataInsertSchemas, SymbolDataUpdateSchemas

from app.tasks.checkBigVolume import checkBigVolumeTasks


celery_log = get_task_logger(__name__)


def symbolSave(db: Session, dataIn: dict):
    repo = SymbolRepository(db)
    id = repo.parse_id(dataIn)
    data = repo.get(id)
    if data is not None:
        if not data.candle_closed:
            data_update = SymbolDataUpdateSchemas(**dataIn)
            data_update.updated_at = datetime.now()
            repo.update(id, data_update.model_dump())
    else:
        dataIn["created_at"] = datetime.now()
        SymbolRepository(db).create(dataIn)

    checkBigVolumeTasks.apply_async(args=[id])


@shared_task(
    bind=True,
    autoretry_for=(Exception,),
    retry_backoff=True,
    retry_kwargs={"max_retries": 3},
    name="tv_dump:symbol_save",
)
def symbolSaveTasks(self, dataIn: dict):
    with engine_db.begin() as connection:
        with Session(bind=connection) as db:
            symbolSave(db, dataIn)
