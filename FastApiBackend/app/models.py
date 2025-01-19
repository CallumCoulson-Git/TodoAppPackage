from sqlmodel import SQLModel, Field, Relationship
from pydantic import EmailStr, validator
from datetime import datetime
from typing import Optional, List
from dateutil.parser import isoparse

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: EmailStr = Field(unique=True, index=True)
    created_at: datetime = Field(default_factory=datetime.now, index=True)
    hashed_password: str
    is_active: bool
    reserves: Optional[List["Reserve"]] = Relationship(back_populates="owner", cascade_delete=True)

    class Config:
        arbitrary_types_allowed = True

class Reserve(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    created_at: datetime = Field(default_factory=datetime.now, index=True)
    set_for: Optional[datetime] = Field(default=None, index=True)
    owner_id: Optional[int] = Field(default=None, foreign_key="user.id")
    owner: Optional[User] = Relationship(back_populates="reserves")

    @validator('set_for', pre=True, always=True)
    def parse_set_for(cls, value):
        if isinstance(value, str):
            return isoparse(value)
        return value

    class Config:
        arbitrary_types_allowed = True
