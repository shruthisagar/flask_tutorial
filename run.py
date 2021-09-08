
from flask import Flask, Blueprint
app = Flask(__name__)

from flask.json import JSONEncoder

from user import user_blueprint
app.register_blueprint(user_blueprint)

from products import products_blueprint
app.register_blueprint(products_blueprint)

@app.before_request
def before_request():
    # request validator goes in
    print("I am in before request")

class AppJSONEncoder(JSONEncoder):

    def default(self, obj):
        from bson import ObjectId
        if isinstance(obj, ObjectId):
            return str(obj)
        else:
            return JSONEncoder.default(self, obj)

app.json_encoder = AppJSONEncoder

@app.route("/")
def hello_world():
    return "Hello World!"

if __name__ == "__main__":
    app.run(debug=True)
