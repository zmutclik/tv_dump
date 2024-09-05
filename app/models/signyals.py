from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Time, TIMESTAMP, DateTime, func, case, Float, text
from sqlalchemy.orm import column_property, relationship, deferred
from app.models.__base import Base


class SignyalTable(Base):
    __tablename__ = "signals"

    id = Column(String(50), primary_key=True, index=True)
    id_symbol = Column(String(50), ForeignKey("symbol.id"))
    symbol = Column(String(50), index=True)
    nama = Column(String(50), index=True)
    waktu = Column(DateTime, index=True)
    method = Column(String(4), nullable=False)

    open = Column(Float)
    sl = Column(Float, default=0)
    tp = Column(Float, default=0)

    status_open = Column(Boolean, default=True)
