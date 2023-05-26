from fastapi import FastAPI , Depends , HTTPException , status
from fastapi.middleware.cors import CORSMiddleware
from hashing import Hash
from pymongo import MongoClient
from bson import ObjectId
import logging
from models import UserIn, UserOut, BlogIn, BlogOut
from typing import List
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

MONGODB_URL = load_dotenv("MONGODB_URL")

client = MongoClient(MONGODB_URL)
db = client["blog"]
collection1 = db["users"]
collection2 = db["blogs"]

async def get_db():
    db = client["blog"]
    yield db

origins = [
    "http://localhost:3000",
    "localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/user", response_model=UserOut , status_code=status.HTTP_201_CREATED , tags=["users"])
async def create_user(user: UserIn, db: MongoClient = Depends(get_db)):
    logger.info("Creating user")
    user = user.dict()
    user["id"] = str(ObjectId())
    user["password"] = Hash.bcrypt(user["password"])
    user_id = collection1.insert_one(user)
    user = collection1.find_one({"_id": user_id.inserted_id})
    return user

@app.get("/user", response_model=List[UserOut] , tags=["users"])
async def get_users(db: MongoClient = Depends(get_db)):
    logger.info("Getting All users")
    users = collection1.find()
    users = list(users)
    return users

@app.get("/user/{user_id}", response_model=UserOut , tags=["users"])
async def get_user(user_id: str, db: MongoClient = Depends(get_db)):
    logger.info("Getting user")
    user = collection1.find_one({"id": user_id})
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/user/{user_id}", tags=["users"])
async def delete_user(user_id: str, db: MongoClient = Depends(get_db)):
    logger.info("Deleting user")
    user = collection1.find_one({"id": user_id})
    if user:
        collection1.delete_one({"id": user_id})
        return {"message": "User deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found")

@app.put("/user/{user_id}", response_model=UserOut , tags=["users"])
async def update_user(user_id: str, user: UserIn, db: MongoClient = Depends(get_db)):
    logger.info("Updating user")
    user = user.dict()
    user = collection1.find_one_and_update({"id": user_id}, {"$set": user}, return_document=True)
    return user

@app.post("/blog", response_model=BlogOut , status_code=status.HTTP_201_CREATED , tags=["blogs"])
async def create_blog(blog: BlogIn, db: MongoClient = Depends(get_db)):
    logger.info("Creating blog")
    blog = blog.dict()
    blog["id"] = str(ObjectId())
    blog_id = collection2.insert_one(blog)
    blog = collection2.find_one({"_id": blog_id.inserted_id})
    return blog

@app.get("/blog", response_model=List[BlogOut] , tags=["blogs"])
async def get_blogs(db: MongoClient = Depends(get_db)):
    logger.info("Getting All blogs")
    blogs = collection2.find()
    blogs = list(blogs)
    return blogs

@app.get("/blog/{blog_id}", response_model=BlogOut , tags=["blogs"])
async def get_blog(blog_id: str, db: MongoClient = Depends(get_db)):
    logger.info("Getting blog")
    blog = collection2.find_one({"id": blog_id})
    if blog:
        return blog
    raise HTTPException(status_code=404, detail="Blog not found")

@app.delete("/blog/{blog_id}", tags=["blogs"])
async def delete_blog(blog_id: str, db: MongoClient = Depends(get_db)):
    logger.info("Deleting blog")
    blog = collection2.find_one({"id": blog_id})
    if blog:
        collection2.delete_one({"id": blog_id})
        return {"message": "Blog deleted successfully"}
    raise HTTPException(status_code=404, detail="Blog not found")

@app.put("/blog/{blog_id}", response_model=BlogOut , tags=["blogs"])
async def update_blog(blog_id: str, blog: BlogIn, db: MongoClient = Depends(get_db)):
    logger.info("Updating blog")
    blog = blog.dict()
    blog = collection2.find_one_and_update({"id": blog_id}, {"$set": blog}, return_document=True)
    if blog:
        return blog
    raise HTTPException(status_code=404, detail="Blog not found")