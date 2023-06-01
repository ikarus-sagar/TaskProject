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
        duplicate_user = create_user(user)
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
        duplicate_blog = create_blog(blog)
    except HTTPException as e:
        assert e.status_code == status.HTTP_400_BAD_REQUEST
        assert e.detail == "Blog with the same title already exists"
    finally:
        delete_blog(created_blog["id"])


def test_update_user_information():
    user = UserIn(
        name="test",
        email="test@gmail.com",
        password="test123"
    )
    created_user = create_user(user)
    updated_user = UserIn(
        name="updated_test",
        email="updated_test@gmail.com"
    )
    updated_user_id = update_user(created_user["id"], updated_user)
    retrieved_user = get_user(updated_user_id)
    assert retrieved_user["name"] == "updated_test"
    assert retrieved_user["email"] == "updated_test@gmail.com"
    delete_user(created_user["id"])


def test_delete_user():
    user = UserIn(
        name="test",
        email="test@gmail.com",
        password="test123"
    )
    created_user = create_user(user)
    delete_user(created_user["id"])
    try:
        retrieved_user = get_user(created_user["id"])
    except HTTPException as e:
        assert e.status_code == status.HTTP_404_NOT_FOUND
        assert e.detail == "User not found"


def test_retrieve_specific_blog():
    blog = BlogIn(
        title="test",
        content="test",
        creator="test"
    )
    created_blog = create_blog(blog)
    retrieved_blog = get_blog(created_blog["id"])
    assert retrieved_blog["title"] == "test"
    assert retrieved_blog["content"] == "test"
    assert retrieved_blog["creator"] == "test"
    delete_blog(created_blog["id"])


def test_retrieve_all_blogs():
    blog1 = BlogIn(
        title="blog1",
        content="content1",
        creator="creator1"
    )
    blog2 = BlogIn(
        title="blog2",
        content="content2",
        creator="creator2"
    )
    create_blog(blog1)
    create_blog(blog2)
    blogs = get_blogs()
    assert len(blogs) == 2
    delete_blog(blogs[0]["id"])
    delete_blog(blogs[1]["id"])


def test_update_blog_content():
    blog = BlogIn(
        title="test",
        content="test",
        creator="test"
    )
    created_blog = create_blog(blog)
    updated_blog = BlogIn(
        content="updated_content"
    )
    updated_blog_id = update_blog(created_blog["id"], updated_blog)
    retrieved_blog = get_blog(updated_blog_id)
    assert retrieved_blog["content"] == "updated_content"
    delete_blog(created_blog["id"])


def test_delete_blog():
    blog = BlogIn(
        title="test",
        content="test",
        creator="test"
    )
    created_blog = create_blog(blog)
    delete_blog(created_blog["id"])
    try:
        retrieved_blog = get_blog(created_blog["id"])
    except HTTPException as e:
        assert e.status_code == status.HTTP_404_NOT_FOUND
        assert e.detail == "Blog not found"
