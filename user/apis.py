from flask import Blueprint, jsonify, request
from .controllers import UserFunctions

user_blueprint = Blueprint('user',  __name__, url_prefix="/user", )

@user_blueprint.route("/", methods=['GET'])
def user():
    return jsonify(UserFunctions().get_users())

@user_blueprint.route("/<email_id>", methods=['GET'])
def get_user_by_email(email_id):
    response, status_code = UserFunctions().get_user_by_email(email_id)
    return jsonify(response), status_code

@user_blueprint.route("/", methods=["POST"])
def insert_user():
    response, status_code = UserFunctions().insert_user(request.json)
    return jsonify(response), status_code
