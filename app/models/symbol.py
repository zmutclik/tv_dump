from sqlalchemy import Column, Integer, String, Date, Time, Float, DateTime
from app.core.database import Base



class Euro05Table(Base):
    __tablename__ = "symbol_eur_05"

    waktu = Column(Integer, primary_key=True, index=True)
    open = Column(Float)
    hight = Column(Float)
    low = Column(Float)
    close = Column(Float)


class Euro30Table(Base):
    __tablename__ = "symbol_eur_30"

    waktu = Column(Integer, primary_key=True, index=True)
    open = Column(Float)
    hight = Column(Float)
    low = Column(Float)
    close = Column(Float)
