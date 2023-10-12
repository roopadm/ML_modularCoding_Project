from source.constants import *
from source.logger import logging
from source.exception import CustomException
import os, sys
from source.config.configuration import *
from dataclasses import dataclass
from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression,Lasso,Ridge
from sklearn.svm import SVR
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from source.utlis import evaluate_model,save_obj



@dataclass
class ModelTrainerConfig:
    trained_model_file_path=MODEL_FILE_PATH


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()

    def initiate_model_training(self,train_array,test_array):
        try:
            logging.info("Splitting dependent and independent variables from train and test data")
            X_train,y_train,X_test,y_test=(train_array[:,:-1],train_array[:,-1],
                                           test_array[:,:-1],test_array[:,-1])

            models={
                'Linear Regression':LinearRegression(),
                'DecisionTree':DecisionTreeRegressor(),
                'Random Forest':RandomForestRegressor(),
                'Gradient Boosting':GradientBoostingRegressor(),
                'XGB Regressor':XGBRegressor(),
                "Ridge":Ridge(),
                 "SVR":SVR()
            }      

            model_report: dict=evaluate_model(X_train,y_train,X_test,y_test,models)
            print("model report")
            print("\n =================================================\n")
            logging.info(f'Model Report :{model_report}')


            # best model by sorting models based on score and choosing best 

            best_model_score=max(sorted(model_report.values()))

            best_model_name=list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]

            best_model=models[best_model_name]

            print(f'Found best model, Model name is :{best_model_name},with R2 score :{best_model_score}')
            print('\n ============================================================\n')
            logging.info(f'Found best model, Model name is :{best_model_name},with R2 score :{best_model_score}')

            save_obj(file_path=self.model_trainer_config.trained_model_file_path,
                     obj=best_model)
            
        except Exception as e:
            logging.info('Exception occured at Model training')
            raise CustomException(e,sys)