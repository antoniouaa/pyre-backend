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
    if results:
        response = [
            {
                "id": feed_id,
                "title": title,
                "link": link,
                "date_added": date_added,
                "description": description,
            }
            for feed_id, title, link, date_added, description in results
        ]
        return jsonify(response), 200
    else:
        return jsonify(message="Empty Database", statusCode=404), 404


@app.route("/feeds/add", methods=["POST"])
def add_feed():
    name = request.form.get("name")
    link = request.form.get("link")
    status = db.add_new_feed(name, link)
    if status:
        return jsonify(message="Success", statusCode=201), 201
    else:
        return jsonify(message="Failure to post", statusCode=404), 404


@app.route("/feeds/<name>")
def get_feed(name):
    response = db.get_feed_by_name(name)
    if response:
        return jsonify(response), 200
    else:
        return jsonify(message="Feed not found", statusCode=404), 404


@app.route("/feeds/delete/<name>", methods=["DELETE"])
def delete_feed(name):
    response = db.delete_feed(name)
    if response:
        return jsonify(message="Delete successful", statusCode=204), 204
    else:
        return jsonify(message="Feed not found", statusCode=404), 404
