from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello Tutorial!"


@app.route("/name")
def print_name():
    return "Hello " + request.args.get("name", "World!")


@app.route("/add_user", methods=["POST"])
def add_user():
    from users import insert_user
    result = insert_user(request.json)
    return result


@app.route("/update_user", methods=["PUT"])
def update_user():
    from users import update_user
    result = update_user(request.args.get("id"), request.json)
    return "updated"


@app.route("/find_user", methods=["POST"])
def find_user():
    from users import find_user
    result = find_user(request.json)
    return result


if __name__ == "__main__":
    app.run(debug=True)
