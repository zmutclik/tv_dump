from celery import shared_task
from sqlalchemy.orm import Session
from celery.utils.log import get_task_logger

from app.core.database import engine_db
from app.repositories import SymbolRepository

from app.schemas.symbol import SymbolDataInsertSchemas, SymbolDataUpdateSchemas


celery_log = get_task_logger(__name__)


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
            repo = SymbolRepository(db)
            id = repo.parse_id(dataIn.model_dump())
            data = repo.get(id)
            if data is not None:
                data_update = SymbolDataUpdateSchemas.model_validate(
                    dataIn.model_dump()
                )
                repo.update(id, data_update.model_dump())
            else:
                SymbolRepository(db).create(dataIn.model_dump())
