#!/usr/bin/env python3

from flask import Flask, jsonify
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)


@app.errorhandler(401)
def unauthorized_error(error):
    """
    Handles 401 Unauthorized errors.

    Returns:
        JSON response with the error message.
    """
    return jsonify({"error": "Unauthorized"}), 401


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
