from typing import Annotated, Union
from datetime import timedelta

from fastapi import APIRouter, Request, Response, Depends, Cookie, Security
from sqlalchemy.orm import Session

from app.schemas.symbol import SymbolDataInsertSchemas
from app.tasks.symbolSave import symbolSaveTasks

router = APIRouter(prefix="", tags=["symbol"])


@router.post("/symbol")
async def root(
    dataIn: SymbolDataInsertSchemas,
):
    symbolSaveTasks.apply_async(args=[dataIn.model_dump()])
