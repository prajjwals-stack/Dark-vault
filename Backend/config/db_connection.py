from pymongo import MongoClient
# from config.config import MONGO_COULD_CLIENT,MONGO_CLOUD_DATABASE


m_client = MongoClient("mongodb://localhost:27017")
db = m_client["dark_vault"]

# db["user management"].insert_one({"test":"test"})