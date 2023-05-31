from fastapi import APIRouter, Depends, HTTPException, status
from pymongo import MongoClient
from bson import ObjectId
from models.user_models import UserIn, UserOut
from typing import List
from config.secrets_parser import *
from config.logging import logger
from utils.hashing import Hash
from config.secrets_parser import *

router = APIRouter()
users_collection = get_users_collection()

@router.post("/user", status_code=status.HTTP_201_CREATED, tags=["users"])
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


@router.get("/user", response_model=List[UserOut], status_code=status.HTTP_200_OK, tags=["users"])
def get_users(db: MongoClient = Depends(get_database)):
    logger.info("Getting All users")
    users = users_collection.find()
    users = list(users)
    if users:
        return users
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No users found")


@router.get("/user/{user_id}", response_model=UserOut, status_code=status.HTTP_200_OK, tags=["users"])
def get_user(user_id: str, db: MongoClient = Depends(get_database)):
    logger.info("Getting user")
    user = users_collection.find_one({"id": user_id})
    if user:
        return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")


@router.delete("/user/{user_id}", status_code=status.HTTP_202_ACCEPTED, tags=["users"])
def delete_user(user_id: str, db: MongoClient = Depends(get_database)):
    logger.info("Deleting user")
    user = users_collection.find_one({"id": user_id})
    if user:
        users_collection.delete_one({"id": user_id})
        return {
            "message": "User with id: {} deleted successfully".format(user_id)
        }
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")


@router.put("/user/{user_id}", status_code=status.HTTP_200_OK, tags=["users"])
def update_user(user_id: str, user: UserIn, db: MongoClient = Depends(get_database)):
    logger.info("Updating user")
    user = user.dict()
    user["password"] = Hash.bcrypt(user["password"])
    user = users_collection.find_one_and_update({"id": user_id}, {"$set": user}, return_document=True)
    if user:
        return user["id"]
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")