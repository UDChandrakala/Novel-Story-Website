import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

client = pymongo.MongoClient(
    os.environ.get("MONGO_URI")
)

print(client.list_database_names())