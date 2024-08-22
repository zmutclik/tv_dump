from typing import Annotated, Union
from datetime import timedelta

from fastapi import APIRouter, Request, Response, Depends, Cookie, Security
from sqlalchemy.orm import Session

from app.schemas.symbol import SymbolDataInsertSchemas, SymbolDataUpdateSchemas
from app.core.database import get_db
from app.repositories import SymbolRepository

router = APIRouter(prefix="", tags=["symbol"])


@router.post("/symbol")
async def root(
    dataIn: SymbolDataInsertSchemas,
    db: Session = Depends(get_db),
):
    SymbolRepository(db).create(dataIn.model_dump())


@router.post("/symbol/1")
async def root(
    dataIn: SymbolDataInsertSchemas,
    db: Session = Depends(get_db),
):
    repo = SymbolRepository(db)
    id = repo.parse_id(dataIn.model_dump())
    print(id)
    dataIn.waktu = dataIn.waktu - timedelta(minutes=dataIn.timeframe)
    id = repo.parse_id(dataIn.model_dump())
    print(id)
    data = repo.get(id)
    if data is not None:
        data_update = SymbolDataUpdateSchemas.model_validate(dataIn)
        repo.update(id, data_update.model_dump())
