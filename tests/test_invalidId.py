from fastapi import HTTPException, status
from routes.blog_routes import *
from routes.user_routes import *

def test_update_user_invalid_id():
    try:
        updated_user = update_user("invalid_id", UserIn(
            name="test",
            email="test@gmail.com",
            password="test123"
        ))
    except HTTPException as e:
        assert e.status_code == status.HTTP_404_NOT_FOUND
        assert e.detail == "User not found"


def test_update_blog_invalid_id():
    try:
        updated_blog = update_blog("invalid_id", BlogIn(
            title="test",
            content="test",
            creator="test"
        ))
    except HTTPException as e:
        assert e.status_code == status.HTTP_404_NOT_FOUND
        assert e.detail == "Blog not found"


def test_delete_user_invalid_id():
    try:
        delete_user("invalid_id")
    except HTTPException as e:
        assert e.status_code == status.HTTP_404_NOT_FOUND
        assert e.detail == "User not found"


def test_delete_blog_invalid_id():
    try:
        delete_blog("invalid_id")
    except HTTPException as e:
        assert e.status_code == status.HTTP_404_NOT_FOUND
        assert e.detail == "Blog not found"