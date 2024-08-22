from sqlalchemy import Column, Integer, String, Date, Time, Float, DateTime
# from app.core.database import Base

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class SymbolTable(Base):
    __tablename__ = "symbol"

    id = Column(String(50), primary_key=True, index=True)
    symbol = Column(String(50), index=True)
    timeframe = Column(Integer, index=True)
    waktu = Column(DateTime, index=True)
    waktu_date = Column(Date, index=True)
    waktu_time = Column(Time, index=True)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volume = Column(Float)
    volume_ma = Column(Float)
    volume_delta = Column(Float)
