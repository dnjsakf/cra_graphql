from flask import Blueprint, jsonify
from flask_graphql import GraphQLView

app = Blueprint('sample', __name__)

@app.route("/data", methods=["GET"])
def index():
  return jsonify({
    "data": {
      "users": [
        { "name": "heo", "age": 29, "gender": "M" },
        { "name": "jeong", "age": 2, "gender": "F" },
        { "name": "un", "age": 3, "gender": "M" }
      ]
    }
  }), 200