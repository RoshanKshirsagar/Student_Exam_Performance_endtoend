import os,sys
from student import utils
from student.logger import logging
from student.exception import StudentException
from student.entity import config_entity, artifact_entity

import pandas as pd
import numpy as np 
from sklearn.model_selection import train_test_split


class DataIngestion:
    
    def __init__(self, data_ingestion_config: config_entity.DataIngestionConfig):
        try:
            self.data_ingestion_config=data_ingestion_config
        except Exception as e:
            raise SensorException(e,sys)
   
    def initiate_data_ingestion(self)->artifact_entity.DataIngestionArtifact:
        try:
            logging.info(f"Exporting collection data as pandas dataframe")

            df:pd.DataFrame = utils.get_collection_as_dataframe(
                database_name=self.data_ingestion_config.database_name,
                collection_name=self.data_ingestion_config.collection_name)

            # replace na with NAN
            df.replace(to_replace='na',value=np.NAN, inplace=True)

            # Save data in feature store
            logging.info(f"Save data in feature store")
            # Create feature store if not available
            feature_store_dir = os.path.dirname(self.data_ingestion_config.feature_store_file_path)
            os.makedirs(feature_store_dir, exist_ok=True)

            # Save df to feature store folder
            logging.info(f"Save df to feature store folder")
            df.to_csv(path_or_buf= self.data_ingestion_config.feature_store_file_path, index=False, header=True)
            
            # Splitting the dataset into train and test parts
            train_df, test_df = train_test_split(df, test_size=self.data_ingestion_config.test_size)

            # Create dataset directory if not available
            logging.info(f"Creating dataset dir if not available")
            dataset_dir = os.path.dirname(self.data_ingestion_config.train_file_path)
            os.makedirs(dataset_dir, exist_ok=True)

            # Save df to feature store folder
            logging.info("Save df to feature store folder")
            train_df.to_csv(path_or_buf= self.data_ingestion_config.train_file_path, index=False,header=True)
            test_df.to_csv(path_or_buf= self.data_ingestion_config.test_file_path, index=False,header=True)

            # Preparing artifacts

            data_ingestion_artifact = artifact_entity.DataIngestionArtifact(
                feature_store_file_path=self.data_ingestion_config.feature_store_file_path, 
                train_file_path=self.data_ingestion_config.train_file_path, 
                test_file_path=self.data_ingestion_config.test_file_path)

            logging.info(f"Data Ingestion artifacts: {data_ingestion_artifact}")

            return data_ingestion_artifact
        
        except Exception as e:
            raise StudentException(error_message=e, error_detail=sys)