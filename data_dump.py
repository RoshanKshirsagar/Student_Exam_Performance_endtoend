import pymongo
import pandas as pd
import json

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017")


DATA_FILE_PATH = "/config/workspace/stud.csv"
DATABASE_NAME = "sep"
COLLECTION_NAME = "student"


if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns : {df.shape}")

    # Convert dataframe to json so that we can dump these record in mongo db
    df.reset_index(drop=True, inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    # inserting json record into mongodb
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)