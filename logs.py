from flask import Flask
from source.logger import logging

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])

def index():
    logging.info("testing logging file")
    
    return "welcome to Machine Learning"

if __name__== "__main__" :
    app.run(debug=True)    # default port_number:5000