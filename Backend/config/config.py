import os
import configparser

parser = configparser.ConfigParser(interpolation=None)
parser.read(os.path.join(os.getcwd(), "config", "config.ini"))

MONGO_COULD_CLIENT=parser["MONGODB_CLOUD"]["MONGO_CLIENT"]
MONGO_CLOUD_DATABASE=parser["MONGODB_CLOUD"]["MONGODB_DATABASE"]
USER_COLLECTION=parser["MONGODB_CLOUD"]["USER_MANAGEMENT"]
PASSWORD_COLLECTION=parser["MONGODB_CLOUD"]["PASSWORD_MANAGEMENT"]
THREE_FA_COLLECTION=parser["MONGODB_CLOUD"]["THREE_FA_MANAGEMENT"]