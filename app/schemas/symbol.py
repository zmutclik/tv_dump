from typing import Union
from pydantic import BaseModel
from datetime import datetime


class SymbolDataUpdateSchemas(BaseModel):
    open: float
    high: float
    low: float
    close: float
    volume: float
    volume_ma: float
    volume_delta: float


class SymbolDataInsertSchemas(SymbolDataUpdateSchemas):
    symbol: str
    timeframe: int
    waktu: datetime
