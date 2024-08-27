from typing import Annotated, Union
from datetime import timedelta

from fastapi import APIRouter, Request, Response, Depends, Cookie, Security
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.symbol import SymbolDataInsertSchemas
from app.tasks.symbolSave import symbolSaveTasks, symbolSave

router = APIRouter(prefix="", tags=["symbol"])


@router.post("/symbol")
async def save_direct(dataIn: SymbolDataInsertSchemas, closed: bool = False, db: Session = Depends(get_db)):
    dataIn.candle_closed = closed
    symbolSave(db, dataIn.model_dump())


@router.post("/symbol/v2")
async def save_background(dataIn: SymbolDataInsertSchemas, closed: bool = False):
    dataIn.candle_closed = closed
    symbolSaveTasks.apply_async(args=[dataIn.model_dump()])
