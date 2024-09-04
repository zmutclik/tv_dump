import os
from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from app.core.env import DB_ENGINE
from app import models

Base = declarative_base()


engine_db = create_engine(DB_ENGINE)
conn_db = engine_db.connect()

SessionLocal = sessionmaker(autocommit=False, autoflush=False)
SessionLocal.configure(
    binds={
        models.SymbolTable: engine_db,
        models.BixVolumeTable: engine_db,
        models.SignyalTable: engine_db,
    }
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
