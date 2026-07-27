from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()


client = MongoClient(
    os.environ.get("MONGO_URI")
)


db = client["novels_db"]

users_collection = db["users"]

stories_collection = db["stories"]