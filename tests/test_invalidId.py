from fastapi import HTTPException, status
from routes.blog_routes import *
from routes.user_routes import *
from config.secrets_parser import get_database
import pytest

def test_update_user_invalid_id():
    with pytest.raises(HTTPException) as e:
        update_user("invalid_id", UserIn(
            name="test",
            email="test@gmail.com",
            password="test123"
        ), get_database())
    assert e.value.status_code == status.HTTP_404_NOT_FOUND
    assert e.value.detail == "User not found"


def test_update_blog_invalid_id():
    with pytest.raises(HTTPException) as e:
        update_blog("invalid_id", BlogIn(
            title="test",
            content="test",
            creator="test"
        ), get_database())
    assert e.value.status_code == status.HTTP_404_NOT_FOUND
    assert e.value.detail == "Blog not found"


def test_delete_user_invalid_id():
    with pytest.raises(HTTPException) as e:
        delete_user("invalid_id", get_database())
    assert e.value.status_code == status.HTTP_404_NOT_FOUND
    assert e.value.detail == "User not found"


def test_delete_blog_invalid_id():
    with pytest.raises(HTTPException) as e:
        delete_blog("invalid_id", get_database())
    assert e.value.status_code == status.HTTP_404_NOT_FOUND
    assert e.value.detail == "Blog not found"
