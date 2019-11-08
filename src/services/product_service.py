from flask import jsonify
from ..models.product import Product
from ..database.product_schema import product_schema
from ..database.product_schema import products_schema


# Get all products
def get_products():
    all_products = Product.query.all()

    return product_schema.jsonify(all_products, many=True)

# def get_products():
#     return "Product service"
