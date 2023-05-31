from fastapi import FastAPI, Depends, HTTPException, status
from util.hashing import Hash
from pymongo import MongoClient
from bson import ObjectId
from models.user_models import UserIn, UserOut
from models.blog_models import BlogIn, BlogOut
from typing import List
from config.secrets_parser import *
from config.logging import logger
from fastapi.staticfiles import StaticFiles


app = FastAPI()

db = get_database()
users_collection = get_users_collection()
blogs_collection = get_blogs_collection()


@app.post("/user", status_code=status.HTTP_201_CREATED, tags=["users"])
def create_user(user: UserIn, db: MongoClient = Depends(get_database)):
    logger.info("Creating user")
    user = user.dict()
    user["id"] = str(ObjectId())
    user["password"] = Hash.bcrypt(user["password"])
    users_collection.insert_one(user)
    return {
        "message": "User created successfully",
        "id": user["id"],
    }


@app.get("/user", response_model=List[UserOut], status_code=status.HTTP_200_OK, tags=["users"])
def get_users(db: MongoClient = Depends(get_database)):
    logger.info("Getting All users")
    users = users_collection.find()
    users = list(users)
    if users:
        return users
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No users found")


@app.get("/user/{user_id}", response_model=UserOut, status_code=status.HTTP_200_OK, tags=["users"])
def get_user(user_id: str, db: MongoClient = Depends(get_database)):
    logger.info("Getting user")
    user = users_collection.find_one({"id": user_id})
    if user:
        return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")


@app.delete("/user/{user_id}", status_code=status.HTTP_202_ACCEPTED, tags=["users"])
def delete_user(user_id: str, db: MongoClient = Depends(get_database)):
    logger.info("Deleting user")
    user = users_collection.find_one({"id": user_id})
    if user:
        users_collection.delete_one({"id": user_id})
        return {
            "message": "User with id: {} deleted successfully".format(user_id)
        }
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")


@app.put("/user/{user_id}", status_code=status.HTTP_200_OK, tags=["users"])
def update_user(user_id: str, user: UserIn, db: MongoClient = Depends(get_database)):
    logger.info("Updating user")
    user = user.dict()
    user["password"] = Hash.bcrypt(user["password"])
    user = users_collection.find_one_and_update({"id": user_id}, {"$set": user}, return_document=True)
    if user:
        return user["id"]
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")



@app.post("/blog", status_code=status.HTTP_201_CREATED, tags=["blogs"])
def create_blog(blog: BlogIn, db: MongoClient = Depends(get_database)):
    logger.info("Creating blog")
    blog = blog.dict()
    blog["id"] = str(ObjectId())
    blogs_collection.insert_one(blog)
    return {
        "message": "Blog created successfully",
        "id": blog["id"],
    }


@app.get("/blog", response_model=List[BlogOut], status_code=status.HTTP_200_OK, tags=["blogs"])
def get_blogs(db: MongoClient = Depends(get_database)):
    logger.info("Getting All blogs")
    blogs = blogs_collection.find()
    blogs = list(blogs)
    if blogs:
        return blogs
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No blogs found")


@app.get("/blog/{blog_id}", response_model=BlogOut, status_code=status.HTTP_200_OK, tags=["blogs"])
def get_blog(blog_id: str, db: MongoClient = Depends(get_database)):
    logger.info("Getting blog")
    blog = blogs_collection.find_one({"id": blog_id})
    if blog:
        return blog
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")


@app.delete("/blog/{blog_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["blogs"])
def delete_blog(blog_id: str, db: MongoClient = Depends(get_database)):
    logger.info("Deleting blog")
    blog = blogs_collection.find_one({"id": blog_id})
    if blog:
        blogs_collection.delete_one({"id": blog_id})
        return {"message": "Blog deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")


@app.put("/blog/{blog_id}", response_model=BlogOut, status_code=status.HTTP_200_OK, tags=["blogs"])
def update_blog(blog_id: str, blog: BlogIn, db: MongoClient = Depends(get_database)):
    logger.info("Updating blog")
    blog = blog.dict()
    blog = blogs_collection.find_one_and_update({"id": blog_id}, {"$set": blog}, return_document=True)
    if blog:
        return blog
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")


app.mount("/", StaticFiles(directory="frontend/build", html=True), name="frontend")