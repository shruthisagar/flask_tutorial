from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"

@app.route("/postData", methods=["POST"])
def post_data():
    return request.json


if __name__ == "__main__":
    app.run(debug=True)
