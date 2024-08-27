from typing import Union
from pydantic import BaseModel, root_validator
from datetime import datetime


class SymbolDataUpdateSchemas(BaseModel):
    open: float
    high: float
    low: float
    close: float
    volume: float
    volume_ma: float
    volume_delta: float
    volume_delta: float

    created_at: datetime = None
    updated_at: datetime = None


class SymbolDataInsertSchemas(SymbolDataUpdateSchemas):
    symbol: str
    timeframe: int
    waktu: datetime
