#!/usr/bin/env python3

from flask import Blueprint, abort

# Define the Blueprint for the app
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')


@app_views.route('/unauthorized', methods=['GET'])
def unauthorized():
    """
    This function handles the /api/v1/unauthorized route.
    It raises a 401 Unauthorized error using the abort function.

    Returns:
        JSON response with the error message.
    """
    abort(401)
