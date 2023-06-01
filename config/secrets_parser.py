import yaml
import pymongo

def get_secrets():
    with open("config/secrets.yml", 'r') as stream:
        secrets = yaml.safe_load(stream)
    return secrets

secrets = get_secrets()

mongodb_host = secrets['mongodb']['host']
mongodb_port = secrets['mongodb']['port']
mongodb_username = secrets['mongodb']['username']
mongodb_password = secrets['mongodb']['password']
mongodb_database = secrets['mongodb']['database'].replace('.', '_')

def get_database():
    client = pymongo.MongoClient(mongodb_host, mongodb_port)
    return client[mongodb_database]

def get_blogs_collection():
    db = get_database()
    return db["blogs"]

def get_users_collection():
    db = get_database()
    return db["users"]
