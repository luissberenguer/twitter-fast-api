# Python
from uuid import UUID
from datetime import date, datetime
from typing import Optional, List
import json

# Pydantic
from pydantic import BaseModel, EmailStr
from pydantic import Field

# FastAPI

from fastapi import FastAPI, status
from fastapi import Body

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


class UserRegister(User):
    password: str = Field(
        ...,
        min_length=8,
        max_length=150
    )


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


# Path Operations

# Users

# Register a user
@app.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register a User",
    tags=["Users"]
)
def signup(user: UserRegister = Body(...)):
    """
    SignUp

    This path operation registers a user in the app

    Parameters:
        - Request body parameters
            - user: UserRegister
    Return a json with the basic user information:
        - user id: UUID
        - email: EmailStr
        - first_name: str
        - last_name: str
        - birth_data: datetime
    """
    with open("users.json", "r+", encoding="utf-8") as f:
        results = json.loads(f.read())
        user_dict = user.dict()
        user_dict["user_id"] = str(user_dict["user_id"])
        user_dict["birth_date"] = str(user_dict["birth_date"])
        results.append(user_dict)
        f.seek(0)
        f.write(json.dumps(results))
        return user


# Login a User
@app.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Login a User",
    tags=["Users"]
)
def login():
    pass

# Show all users


@app.get(
    path="/users",
    response_model=List(User),
    status_code=status.HTTP_200_OK,
    summary="Show all User",
    tags=["Users"]
)
def show_all_users():
    """
    This Path Operations shows all users un the app

    Parameters:
        -

    Return a json list with all users in the app, with the following keys:
        - user id: UUID
        - email: EmailStr
        - first_name: str
        - last_name: str
        - birth_data: datetime
    """
    with open("users.json", "r", enconding="utf-8") as f:
        results = json.loads(f.read())
        return results

# Show a user


@app.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Register a User",
    tags=["Users"]
)
def show_user():
    pass


# Delete a user
@app.delete(
    path="/users/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete a User",
    tags=["Users"]
)
def delete_user():
    pass


# Update a user
@app.put(
    path="/users/{user_id}/update",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update a User",
    tags=["Users"]
)
def signup():
    pass


# Tweets

# Show all Tweets
@app.get(
    path="/",
    response_model=List(Tweet),
    status_code=status.HTTP_200_OK,
    summary="Show all Tweets",
    tags=["Tweets"]
)
def home():
    return {"Twitter API": "Working!"}


# Post a Tweet
@app.post(
    path="/post",
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary="Post a Tweet",
    tags=["Tweets"]
)
def home(tweet: Tweet = Body(...)):
    pass

# Show a Tweet


@app.get(
    path="/tweet/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Show a Tweet",
    tags=["Tweets"]
)
def show_tweet():
    pass


# Delte a Tweet
@app.delete(
    path="/tweets/{twwet_id}/delete",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Delete a Tweet",
    tags=["Tweets"]
)
def delete_tweet():
    pass


# Update a Tweet
@app.put(
    path="/tweet/{tweet_id}/update",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Update a Tweet",
    tags=["Tweets"]
)
def update_tweet():
    pass
