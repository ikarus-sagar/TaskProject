from fastapi import HTTPException, status
from routes.blog_routes import *
from routes.user_routes import *

def test_user_not_found():
    try:
        user = get_user("non_existing_id")
    except HTTPException as e:
        assert e.status_code == status.HTTP_404_NOT_FOUND
        assert e.detail == "User not found"


def test_blog_not_found():
    try:
        blog = get_blog("non_existing_id")
    except HTTPException as e:
        assert e.status_code == status.HTTP_404_NOT_FOUND
        assert e.detail == "Blog not found"


def test_update_user_not_found():
    try:
        updated_user = update_user("non_existing_id", UserIn(
            name="test",
            email="test@gmail.com",
            password="test123"
        ))
    except HTTPException as e:
        assert e.status_code == status.HTTP_404_NOT_FOUND
        assert e.detail == "User not found"


def test_update_blog_not_found():
    try:
        updated_blog = update_blog("non_existing_id", BlogIn(
            title="test",
            content="test",
            creator="test"
        ))
    except HTTPException as e:
        assert e.status_code == status.HTTP_404_NOT_FOUND
        assert e.detail == "Blog not found"


def test_delete_user_not_found():
    try:
        delete_user("non_existing_id")
    except HTTPException as e:
        assert e.status_code == status.HTTP_404_NOT_FOUND
        assert e.detail == "User not found"


def test_delete_blog_not_found():
    try:
        delete_blog("non_existing_id")
    except HTTPException as e:
        assert e.status_code == status.HTTP_404_NOT_FOUND
        assert e.detail == "Blog not found"