from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Time, TIMESTAMP, DateTime, func, case, Float, text
from sqlalchemy.orm import column_property, relationship, deferred
from app.models.__base import Base


class BixVolumeTable(Base):
    __tablename__ = "bigvolume"

    id = Column(String(50), primary_key=True, index=True)
    id_symbol = Column(String(50), ForeignKey("symbol.id"))
    status_open = Column(Boolean, default=True)
    message_id = Column(Integer)
    
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, nullable=False)

    SYMBOLS = relationship("SymbolTable", back_populates="BIGVOLUME")
