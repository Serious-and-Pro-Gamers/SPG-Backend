from ..models.product import Product
from ..schemas.product_schema import *


# Get all products
def get_products():
    all_products = Product.query.all()
    return product_schema.jsonify(all_products, many=True)
