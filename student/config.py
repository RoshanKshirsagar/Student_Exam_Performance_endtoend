import pymongo
import pandas as pandas
import json


from dataclasses import dataclass
import os

@dataclass
class EnvironmentVariable:
    mongo_db_url:str = os.getenv("MONGO_DB_URL")
    aws_access_key_id:str = os.getenv("AWS_ACCESS_KEY")
    aws_secret_access_key:str = os.getenv("AWS_SECRET_KEY_ID")             



env_var = EnvironmentVariable()

mongo_client = pymongo.MongoClient(env_var.mongo_db_url)