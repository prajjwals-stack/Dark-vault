from pymongo import MongoClient
# from config.config import MONGO_COULD_CLIENT,MONGO_CLOUD_DATABASE


m_client = MongoClient("mongodb+srv://Prajjwal:nah1EXg9a0yPtkYX@darkvault.kid77gv.mongodb.net/?retryWrites=true&w=majority")
db = m_client["dark_vault"]

# db["user management"].insert_one({"test":"test"})