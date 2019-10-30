"""
TEst
"""

from flask import Blueprint

product_api = Blueprint("product_api", __name__)

from services.product_service import get_products


# @product_api.route("/product", methods=["GET"])
# def get_product():
#     return "Product Controller"


@product_api.route("/product", methods=["GET"])
def get_product():
    """Test"""
    return get_products()
