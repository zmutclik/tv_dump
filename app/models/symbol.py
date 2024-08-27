from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Time, TIMESTAMP, DateTime, func, case, Float, text
from sqlalchemy.orm import column_property, relationship, deferred
from app.models.__base import Base


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
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, nullable=False)

    BIGVOLUME = relationship("BixVolumeTable", back_populates="SYMBOLS")
