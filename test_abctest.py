from main import UserIn,BlogIn ,logger ,create_user ,get_users ,get_user ,delete_user ,update_user ,create_blog ,get_blogs ,get_blog ,delete_blog ,update_blog 

def test_user():
    user = UserIn(
        name="test",
        email="test@gmail.com",
        password="test123"
    )
    user = create_user(user)
    user = get_user(user["id"])
    assert user["name"] == "test"
    assert user["email"] == "test@gmail.com"
    assert user["password"] != "test123"
    delete_user(user["id"])
    

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
    for user in users:
        create_user(user)
    users = get_users()
    logger.info(users)
    for user in users:
        if user["name"] in ["test1", "test2"]:
            assert user["name"] in ["test1", "test2"]
            assert user["email"] in ["test1@gmail.com", "test2@gmail.com"]
            delete_user(user["id"])

def test_update_user():
    user = UserIn(
        name="test",
        email="test@gmail.com",
        password="test123"
    )
    user = create_user(user)
    user = update_user(user["id"], UserIn(
        name="test1",
        email="test1@gmail.com",
        password="test123"
    ))
    assert user["name"] == "test1"
    assert user["email"] == "test1@gmail.com"
    delete_user(user["id"])


def test_blog():
    blog = BlogIn(
        title="test",
        content="test",
        creator="test"
    )
    blog = create_blog(blog)
    blog = get_blog(blog["id"])
    assert blog["title"] == "test"
    assert blog["content"] == "test"
    assert blog["creator"] == "test"
    delete_blog(blog["id"])

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
    for blog in blogs:
        create_blog(blog)
    blogs = get_blogs()
    logger.info(blogs)
    for blog in blogs:
        if blog["title"] in ["test1", "test2"]:
            assert blog["title"] in ["test1", "test2"]
            assert blog["content"] in ["test1", "test2"]
            assert blog["creator"] in ["test1", "test2"]
            delete_blog(blog["id"])

def test_update_blog():
    blog = BlogIn(
        title="test",
        content="test",
        creator="test"
    )
    blog = create_blog(blog)
    blog = update_blog(blog["id"], BlogIn(
        title="test1",
        content="test1",
        creator="test1"
    ))
    assert blog["title"] == "test1"
    assert blog["content"] == "test1"
    assert blog["creator"] == "test1"
    delete_blog(blog["id"])