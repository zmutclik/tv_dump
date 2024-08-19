import os

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Time, TIMESTAMP, DateTime, func, case, Float, text
from sqlalchemy.orm import column_property, relationship, deferred, Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property

from ..core import Base


class UsersTable(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(32), unique=True, index=True)
    email = Column(String(50), unique=True, index=True)
    full_name = Column(String(50))
    hashed_password = Column(String(256))
    unlimited_token_expires = Column(Boolean, default=False)
    disabled = Column(Boolean, default=False)

    created_at = Column(TIMESTAMP, nullable=False, server_default=func.now())
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)
    created_user = Column(String(50), nullable=False)
    deleted_user = Column(String(50))

    SCOPES = relationship("UserScopeTable", back_populates="USER")
