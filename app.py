from flask import Flask
import sys
from housing.logger import logging
from housing.exception import HousingException

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def index():
    try:
        raise Exception("we are testing custom expection")
    except Exception as e:
        housing = HousingException(e,sys)
        logging.info(housing.error_message)    
        logging.info("We are testing the logging module")
    return " Starting my machine learning project journey. Added CI/CD pipleine as well"
if __name__ == "__main__":
    app.run(debug=True)
