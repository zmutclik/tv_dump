from typing import Annotated, Union

from fastapi import APIRouter, Request, Response, Depends, Cookie, Security
from sqlalchemy.orm import Session

from app.schemas.symbol import SymbolDataInsertSchemas
from app.core.database import get_db
from app.repositories import SymbolRepository

router = APIRouter(prefix="", tags=["symbol"])


@router.post("/symbol")
async def root(
    dataIn: SymbolDataInsertSchemas,
    request: Request,
    db: Session = Depends(get_db),
):
    SymbolRepository(db).create(dataIn.model_dump())
