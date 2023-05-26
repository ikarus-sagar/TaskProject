from pydantic import BaseModel
from typing import Optional
class Blog(BaseModel):
    id: str
    title: str
    content: str
    creator: str

class User(BaseModel):
    id: str
    name: str
    email: str
    password: str

class UserIn(BaseModel):
    name: str
    email: str
    password: str
    class Config:
        orm_mode = True

class UserOut(BaseModel):
    id: str
    name: str
    email: str
    password: str
    class Config:
        orm_mode = True

class BlogIn(BaseModel):
    title: str
    content: str
    creator: str
    class Config:
        orm_mode = True

class BlogOut(BaseModel):
    id : str
    title: str
    content: str
    creator: str
    class Config:
        orm_mode = True

