import os,sys
from datetime import datetime


# artifact folder -> pipeline folder ->with timestamp->pipleine output 


#def get_current_time_stamp():
    #return f"{datetime.now().strftime('%Y-%m-%d-%H:%M:%S')}"

def get_current_time_stamp():
    return f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}"



CURRENT_TIME_STAMP=get_current_time_stamp()

#ML_MODULARCODING_PROJECT/DATA_DIR/DATA_DIR_KEY
ROOT_DIR_KEY=os.getcwd()
DATA_DIR="data"
DATA_DIR_KEY="delivery_data_2023.csv"


ARTIFACT_DIR_KEY="Artifact"


### Data Ingestion ######
## Artifact/data ingestion/raw_data_dir->raw.csv and Artificat/data ingestion/ingested_dir ->train.csv and test.csv
# Data ingestion related variables
DATA_INGESTION_KEY="data_ingestion"
#step 1-> fetch the data
DATA_INGESTION_KEY_RAW_DATA_DIR="raw_data_dir"
RAW_DATA_DIR_KEY="raw.csv"

# after featching we split the data intro train set and test set
DATA_INGESTION_INGESTED_DATA_DIR_KEY="ingested_dir"
TRAIN_DATA_DIR_KEY="train.csv"
TEST_DATA_DIR_KEY="test.csv"



### Data Transformation #####
## artifact(folder)/data transformation/ data preprocessor->processor.pkl and /data transformation->train.csv and test.csv

DATA_TRANSFORMATION_ARTIFACT="data_transformation"
DATA_PREPROCESS_DIR="process_data"
DATA_PREPROCESS_OBJ="processor.pkl"
DATA_TRANSFORMATION_DIR="transform_data"
TRANSFORM_TRAIN_KEY="train.csv"
TRANSFORM_TEST_KEY="test.csv"
