from pymongo import MongoClient
from dotenv import load_dotenv
import os


load_dotenv()

mongo_uri = os.getenv("MONGO_URI")
database_name = os.getenv("DATABASE_NAME")

client = MongoClient(mongo_uri, tlsAllowInvalidCertificates=True)
db = client[database_name]
todos_collection = db["todos"]
