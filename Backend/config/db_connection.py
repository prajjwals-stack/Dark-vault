from pymongo import MongoClient
# from config.config import MONGO_COULD_CLIENT,MONGO_CLOUD_DATABASE


m_client = MongoClient("mongodb+srv://Prajjwal:Soni%402310@cluster0.ynjt4nh.mongodb.net/test")
db = m_client["dark_vault"]