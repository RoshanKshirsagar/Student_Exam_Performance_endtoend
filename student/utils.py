import pandas as pd 
from student.config import mongo_client
from student.logger import logging
from student.exception import StudentException
import os, sys

def get_collection_as_dataframe(database_name:str, collection_name:str)->pd.DataFrame:

    """
    Description :- This function return collection as dataframe
    ===========================================================
    Params:-
    database_name: database_name
    collection_name = collection_name
    ===========================================================
    return pandas dataframe
    """

    try:
        logging.info(f"Reading data from database: {database_name} and collection: {collection_name}")
        df = pd.DataFrame(list(mongo_client[database_name][collection_name].find()))
        logging.info(f"Found columns: {df.columns}")
        
        if "_id" in df.columns:
            logging.info(f"Dropping column: _id")
            df = df.drop('_id', axis=1)
        logging.info(f"Rows and columns in df: {df.shape}")
        return df

    except Exception as e:
        raise StudentException(e, sys)
    