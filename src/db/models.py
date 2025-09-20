from typing import Optional

from sqlmodel import SQLModel, Field


class UserBase(SQLModel):
    name: str
    email: str
    password: str
    date: Optional[int] = None
    order: Optional[int] = None


class User(UserBase, table=True):
    id: int = Field(default=None, nullable=False, primary_key=True)


class UserCreate(UserBase):
    pass
