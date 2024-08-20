from typing import Union
from pydantic import BaseModel
from datetime import datetime


class SymbolSchemas(BaseModel):
    symbol: str
    waktu: datetime
    timeframe: int
    open: float
    hight: float
    low: float
    close: float
