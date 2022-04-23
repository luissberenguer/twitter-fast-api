# Python
from uuid import UUID
from datetime import date
from typing import Optional


# Pydantic
from pydantic import BaseModel, EmailStr
from pydantic import Field

# FastAPI

from fastapi import FastAPI

app = FastAPI()

# Models


class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    ),
    birth_date: Optional[date] = Field(default=None)


class UserLogin(UserBase):
    password: str = Field(
        ...,
        min_length=8,
        max_length=150
    )


# class User(UserBase):
#     pass


class Tweet(BaseModel):
    pass


@app.get(path="/")
def home():
    return {"Twitter API": "Working!"}
