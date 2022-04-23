# Python
from optparse import Option
from turtle import update
from uuid import UUID
from datetime import date, datetime
from typing import Optional


# Pydantic
from pydantic import BaseModel, EmailStr
from pydantic import Field

# FastAPI

from fastapi import FastAPI

app = FastAPI()

# Models


class User(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    ),
    birth_date: Optional[date] = Field(default=None)


class UserLogin(User):
    password: str = Field(
        ...,
        min_length=8,
        max_length=150
    )


# class User(UserBase):
#     pass


class Tweet(BaseModel):
    tweet_id: str = Field(...)
    content: str = Field(
        ...,
        max_length=256,
        min_length=1
    )
    created_at: datetime = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field(default=None)
    by: User = Field(...)


@app.get(path="/")
def home():
    return {"Twitter API": "Working!"}
