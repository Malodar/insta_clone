from pydantic import BaseModel
from datetime import datetime
from typing import List


class UserBase(BaseModel):      # what we send to API
    username: str
    email: str
    password: str


class UserDisplay(BaseModel):   # what db should return
    username: str
    email: str

    class Config():
        orm_mode = True


class PostBase(BaseModel):
    image_url: str
    image_url_type: str
    caption: str
    creator_id: int


class User(BaseModel):      # for PostDisplay
    username: str
    class Config():
        orm_mode = True

class Comment(BaseModel):    # for PostDisplay
    text: str
    username: str
    timestamp: datetime

    class Config():
        orm_mode = True

class PostDisplay(BaseModel):
    id: int
    image_url: str
    image_url_type: str
    caption: str
    timestamp: datetime
    user: User
    comments: List[Comment]
    class Config():
        orm_mode = True


class UserAuth(BaseModel):
    id: int
    username: str
    email: str


class CommentBase(BaseModel):
    username: str
    text: str
    post_id: int
