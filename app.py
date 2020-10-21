from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)


@app.route("/index")
def index():
    req = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    return jsonify(req.json())


@app.route("/users")
def users():
    req = requests.get("https://jsonplaceholder.typicode.com/users")
    return jsonify(req.json())
