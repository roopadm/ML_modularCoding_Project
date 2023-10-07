from flask import Flask
from source.logger import logging
from source.exception import CustomException
import os, sys

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])

def index():

    try :
        raise Exception("testing Exception file")
    except Exception as e:
       CE= CustomException(e,sys)
       logging.info(CE.error_message)

       logging.info("testing logging file")
    
       return "welcome to Machine Learning"

if __name__== "__main__" :
    app.run(debug=True)    # default port_number:5000