from datetime import datetime
from email.mime import base

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserBase(BaseModel):
    username: str = Field(min_length=1, max_length=50)
    email: EmailStr = Field(max_length=100)


class UserCreate(UserBase):
    password: str = Field(min_length=8)

class UserUpdate(BaseModel):
    username: str | None = Field(default=None, min_length=1, max_length=50)
    email: EmailStr | None = Field(default=None, max_length=100)
    image_file: str | None = Field(default=None, min_length=1, max_length=100)

class Token(BaseModel):
    access_token: str
    token_type: str


class UserResponse(UserBase):
    model_config= ConfigDict(from_attributes=True)
    id: int
    image_file: str | None
    image_path: str


class UserPublic(BaseModel):
    model_config= ConfigDict(from_attributes=True)
    id: int
    username: str
    email: EmailStr
    image_file: str | None
    image_path: str

class UserPrivate(UserPublic):
    email: EmailStr

class PostBase(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    content: str = Field(min_length=1)

class PostCreate(PostBase):
    user_id : int #temporary


class PostUpdate(BaseModel):
    title: str | None = Field(default = None, min_length=1, max_length=100)
    content: str | None = Field(default=None, min_length=1)

class PostResponse(PostBase):  #inherits PostBase and also adds data from the system
    model_config= ConfigDict(from_attributes=True) #allows to read from database
    id: int
    user_id: int
    date_posted: datetime
    author: UserPublic