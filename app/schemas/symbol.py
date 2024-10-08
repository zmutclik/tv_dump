from typing import Union, Optional
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
    volume_delta: float
    candle_closed: Optional[bool] = False

    updated_at: Optional[datetime] = None


class SymbolDataInsertSchemas(SymbolDataUpdateSchemas):
    symbol: str
    timeframe: int
    waktu: datetime
    created_at: Optional[datetime] = None
    
