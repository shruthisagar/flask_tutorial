from flask import Blueprint, jsonify, request
from .controllers import ProductController

products_blueprint = Blueprint('products',  __name__, url_prefix="/products", )

@products_blueprint.route("/list", methods=['GET'])
def products_list():
    return jsonify(ProductController().get_products(request.args)), 200

@products_blueprint.route("/<product_id>", methods=['GET'])
def get_product_by_id(product_id):
    return jsonify(ProductController().get_product_by_id(product_id)),200
