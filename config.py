# config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # MongoDB URI and Database configuration
    MONGO_URI = os.getenv('MONGO_URI')
    MONGO_DBNAME = os.getenv('MONGO_DBNAME')
