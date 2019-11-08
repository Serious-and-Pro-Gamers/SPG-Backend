from ..services.product_service import get_products
from flask import Blueprint


product_api = Blueprint("product_api", __name__)


@product_api.route("/product", methods=["GET"])
def get_product():
    return get_products()
