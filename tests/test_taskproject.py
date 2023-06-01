from models.blog_models import BlogIn
from models.user_models import UserIn
from routes.blog_routes import *
from routes.user_routes import *

def test_user():
    user = UserIn(
        name="test",
        email="test@gmail.com",
        password="test123"
    )
    created_user = create_user(user)
    user_id = created_user["id"]
    try:
        user = get_user(user_id)
        assert user["name"] == "test"
        assert user["email"] == "test@gmail.com"
        assert user["password"] != "test123"
    finally:
        delete_user(user_id)


def test_users():
    users = [
        UserIn(
            name="test1",
            email="test1@gmail.com",
            password="test123"
        ),
        UserIn(
            name="test2",
            email="test2@gmail.com",
            password="test123"
        )
    ]
    created_user_ids = []
    try:
        for user in users:
            created_user = create_user(user)
            created_user_ids.append(created_user["id"])

        users = get_users()
        for user in users:
            if user["name"] in ["test1", "test2"]:
                assert user["name"] in ["test1", "test2"]
                assert user["email"] in ["test1@gmail.com", "test2@gmail.com"]
    finally:
        for user_id in created_user_ids:
            delete_user(user_id)


def test_update_user():
    user = UserIn(
        name="test",
        email="test@gmail.com",
        password="test123"
    )
    new_user = UserIn(
        name="test1",
        email="test1@gmail.com",
        password="test123"
    )
    created_user = create_user(user)
    user_id = created_user["id"]
    try:
        updated_user = update_user(user_id, new_user)
        updated_user = get_user(user_id)
        print(updated_user)
        assert updated_user["name"] == "test1"
        assert updated_user["email"] == "test1@gmail.com"
        assert updated_user["password"] != "test123"
    finally:
        delete_user(user_id)


def test_blog():
    blog = BlogIn(
        title="test",
        content="test",
        creator="test"
    )
    created_blog = create_blog(blog)
    blog_id = created_blog["id"]
    try:
        blog = get_blog(blog_id)
        assert blog["title"] == "test"
        assert blog["content"] == "test"
        assert blog["creator"] == "test"
    finally:
        delete_blog(blog_id)


def test_blogs():
    blogs = [
        BlogIn(
            title="test1",
            content="test1",
            creator="test1"
        ),
        BlogIn(
            title="test2",
            content="test2",
            creator="test2"
        )
    ]
    created_blog_ids = []
    try:
        for blog in blogs:
            created_blog = create_blog(blog)
            created_blog_ids.append(created_blog["id"])

        blogs = get_blogs()
        for blog in blogs:
            if blog["title"] in ["test1", "test2"]:
                assert blog["title"] in ["test1", "test2"]
                assert blog["content"] in ["test1", "test2"]
    finally:
        for blog_id in created_blog_ids:
            delete_blog(blog_id)



def test_delete_users():
    users = get_users()
    for user in users:
        if user["name"] == "test":
            delete_user(user["id"])
            assert 1 == 1
    blogs = get_blogs()
    for blog in blogs:
        if blog["title"] == "test":
            delete_blog(blog["id"])
            assert 1 == 1
