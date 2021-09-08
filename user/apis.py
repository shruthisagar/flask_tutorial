from flask import Blueprint, jsonify
from .controllers import UserFunctions

user_blueprint = Blueprint('user',  __name__, url_prefix="/user", )

@user_blueprint.route("/", methods=['GET'])
def user():
    return jsonify(UserFunctions().get_users())
