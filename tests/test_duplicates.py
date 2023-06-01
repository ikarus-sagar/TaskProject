from fastapi import HTTPException, status
from routes.blog_routes import *
from routes.user_routes import *
from models.blog_models import BlogIn
from models.user_models import UserIn
from config.secrets_parser import get_database
import pytest

def test_create_duplicate_user():
    user = UserIn(
        name="test",
        email="test@gmail.com",
        password="test123"
    )
    created_user = create_user(user, get_database())
    try:
        with pytest.raises(HTTPException) as e:
            create_user(user, get_database())
        assert e.value.status_code == status.HTTP_400_BAD_REQUEST
        assert e.value.detail == "User with the same email already exists"
    finally:
        delete_user(created_user["id"], get_database())


def test_create_duplicate_blog():
    blog = BlogIn(
        title="test",
        content="test",
        creator="test"
    )
    created_blog = create_blog(blog, get_database())
    try:
        with pytest.raises(HTTPException) as e:
            create_blog(blog, get_database())
        assert e.value.status_code == status.HTTP_400_BAD_REQUEST
        assert e.value.detail == "Blog with the same title already exists"
    finally:
        delete_blog(created_blog["id"], get_database())
