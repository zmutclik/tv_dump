from typing import Union
from pydantic import BaseModel
from datetime import datetime


class SymbolDataInsertSchemas(BaseModel):
    symbol: str
    timeframe: int
    waktu: datetime
    open: float
    high: float
    low: float
    close: float
    volume: float
    volume_ma: float
    volume_delta: float
