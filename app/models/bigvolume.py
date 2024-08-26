from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Time, TIMESTAMP, DateTime, func, case, Float, text
from sqlalchemy.orm import column_property, relationship, deferred
from app.models._base import Base


class BixVolumeTable(Base):
    __tablename__ = "bigvolume"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_symbol = Column(String(50), index=True)
    status_open = Column(Boolean, default=True)

    SYMBOLS = relationship("SymbolTable", back_populates="BIGVOLUME")
