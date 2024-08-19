from typing import Generic, TypeVar, List, Optional, Union, Annotated, Any, Dict
from pydantic import BaseModel, Json, Field, EmailStr
from datetime import date, time, datetime

from ..schemas.scope import Scopes


class UserSave(BaseModel):
    username: str
    email: EmailStr
    full_name: str
    hashed_password: str
    created_user: str

class UserSchemas(UserSave):
    id: int

class UserResponse(BaseModel):
    # id: int
    username: str
    email: EmailStr
    full_name: str
    unlimited_token_expires: bool = False
    disabled: bool = False
    SCOPES: list[Scopes]
