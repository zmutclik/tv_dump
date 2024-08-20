from typing import Annotated, Union

from fastapi import APIRouter, Request, Response, Cookie, Security
from app.schemas.symbol import SymbolSchemas

router = APIRouter()


@router.post("/symbol")
async def root(dataIn: SymbolSchemas, request: Request):
    return {"message": "Hello BOZ " + request.client.host + " !!!"}
