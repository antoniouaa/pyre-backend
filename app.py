from flask import Flask, jsonify, request, redirect, url_for
from flask_cors import CORS
import requests

from db import DB

app = Flask(__name__)
CORS(app)

db = DB()


@app.route("/feeds")
def feeds():
    results = db.get_all_feeds()
    response = [{"id": feed_id, "name": name, "link": link}
                for feed_id, name, link in results]
    return jsonify(response)


@app.route("/feeds/add", methods=["POST"])
def add_feed():
    name = request.form.get("name")
    link = request.form.get("link")
    status = db.add_new_feed(name, link)
    print(status)
    if status:
        return jsonify(message="Success", statusCode=201)
