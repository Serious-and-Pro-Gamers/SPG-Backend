import os
import json
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from dotenv import load_dotenv


# from controllers.product_controller import product_api
from controllers.product_controller import product_api

# Init app
app = Flask(__name__)

# Load environment variables
load_dotenv()

# Database variables
DATABASE_USER = os.getenv("SPG_DATABASE_USER")
DATABASE_PASSWORD = os.getenv("SPG_DATABASE_PASSWORD")
DATABASE_ADDRESS = os.getenv("SPG_DATABASE_ADDRESS")
DATABASE_NAME = os.getenv("SPG_DATABASE_NAME")
CONNECTION_STRING = "mysql+pymysql://" + DATABASE_USER + ":" + \
    DATABASE_PASSWORD + "@" + DATABASE_ADDRESS + "/" + DATABASE_NAME

# Database connection
app.config['SQLALCHEMY_DATABASE_URI'] = CONNECTION_STRING
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Init db
db = SQLAlchemy(app)
db.init_app(app)

# Init ma
ma = Marshmallow(app)

# Init cors
cors = CORS(app, resources={r"/*": {"origins": "*"}})


app.register_blueprint(product_api)


# Create a product
# @app.route('/product', methods=['POST'])
# def add_product():
#     name = request.json['name']
#     description = request.json['description']
#     price = request.json['price']
#     qty = request.json['qty']

#     new_product = Product(name, description, price, qty)

#     db.session.add(new_product)
#     db.session.commit()

#     return product_schema.jsonify(new_product)


# Run server
if __name__ == "__main__":
    # Since the host has a wildcard, use the respective urls for dev and prod
    app.run(host='0.0.0.0', debug=True)
