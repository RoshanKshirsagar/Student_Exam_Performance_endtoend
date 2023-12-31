import os
from student.exception import StudentException
from datetime import datetime

FILE_NAME = "student.csv"
TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test.csv"

class TrainingPipelineConfig:
    
    def __init__(self):
        self.artifact_dir = os.path.join(os.getcwd(), 'artifact', datetime.now().strftime("%m_%d_%Y_%H_%M_%S"))

class DataIngestionConfig:

    def __init__(self, training_pipeline_config : TrainingPipelineConfig()):
        try:
            self.database_name = "sep"
            self.collection_name = "student"
            self.data_ingestion_dir = os.path.join(training_pipeline_config.artifact_dir, "data_ingestion")
            self.feature_store_file_path = os.path.join(self.data_ingestion_dir,"feature_store",FILE_NAME)
            self.train_file_path = os.path.join(self.data_ingestion_dir,"dataset", TRAIN_FILE_NAME)
            self.test_file_path = os.path.join(self.data_ingestion_dir,"dataset",TEST_FILE_NAME)
            self.test_size = 0.2
        
        except Exception as e:
            raise StudentException(e, sys)

class DataValidationConfig:...

class DataTransformationConfig:...

class ModelEvaluationConfig:...

class ModelTrainerConfig:...

class ModelPusherConfig:...