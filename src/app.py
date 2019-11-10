import os
from flask_cors import CORS
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


# Initialize flask app
app = Flask(__name__)


# Load environment variables
load_dotenv()


# Get database info from environment variables
DATABASE_USER = os.getenv("SPG_DATABASE_USER")
DATABASE_PASSWORD = os.getenv("SPG_DATABASE_PASSWORD")
DATABASE_ADDRESS = os.getenv("SPG_DATABASE_ADDRESS")
DATABASE_NAME = os.getenv("SPG_DATABASE_NAME")
CONNECTION_STRING = "mysql+pymysql://" + DATABASE_USER + ":" + DATABASE_PASSWORD + "@" + DATABASE_ADDRESS + "/" + DATABASE_NAME


# Set app database connection
app.config['SQLALCHEMY_DATABASE_URI'] = CONNECTION_STRING
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Initialize sqlalchemy
db = SQLAlchemy(app)
db.init_app(app)


# Initialize marshmallow
ma = Marshmallow(app)


# Initialize cors
cors = CORS(app, resources={r"/*": {"origins": "*"}})


# Import needs to be here because it has to load the db connection and marshmallow
from .controllers import product_controller, user_controller


# Initialize controller endpoints
app.register_blueprint(product_controller.product_api)
app.register_blueprint(user_controller.user_api)


# Route for root endpoint <- Yes I did this on purpose
@app.route('/')
def app_route():
    return "Welcome to the SPG API (Work in progress!)"


# Run development server
if __name__ == "__main__":
    # Since the host has a wildcard, use the respective urls for dev and prod
    app.run(host='0.0.0.0', debug=True)
