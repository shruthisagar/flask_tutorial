from flask import Blueprint, jsonify, request
from .controllers import ProductController

products_blueprint = Blueprint('products',  __name__, url_prefix="/products", )

@products_blueprint.route("/", methods=['GET'])
def products():
    return jsonify(ProductController().get_products(request.args)), 200
