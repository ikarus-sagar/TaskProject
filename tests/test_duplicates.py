from fastapi import HTTPException, status
from routes.blog_routes import *
from routes.user_routes import *
from models.blog_models import BlogIn
from models.user_models import UserIn

def test_create_duplicate_user():
    user = UserIn(
        name="test",
        email="test@gmail.com",
        password="test123"
    )
    created_user = create_user(user)
    try:
        create_user(user)
    except HTTPException as e:
        assert e.status_code == status.HTTP_400_BAD_REQUEST
        assert e.detail == "User with the same email already exists"
    finally:
        delete_user(created_user["id"])


def test_create_duplicate_blog():
    blog = BlogIn(
        title="test",
        content="test",
        creator="test"
    )
    created_blog = create_blog(blog)
    try:
        create_blog(blog)
    except HTTPException as e:
        assert e.status_code == status.HTTP_400_BAD_REQUEST
        assert e.detail == "Blog with the same title already exists"
    finally:
        delete_blog(created_blog["id"])
