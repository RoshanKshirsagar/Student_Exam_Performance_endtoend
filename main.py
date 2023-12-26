from student.utils import get_collection_as_dataframe
from student.exception import StudentException
from student.components.data_ingestion import DataIngestion
from student.entity import config_entity


import os,sys

if __name__ == "__main__":
     try:
          training_pipeline_config = config_entity.TrainingPipelineConfig()
          data_ingestion_config = config_entity.DataIngestionConfig(training_pipeline_config = training_pipeline_config)
          data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
          print(data_ingestion.initiate_data_ingestion())
     except Exception as e:
          raise StudentException(e, sys)