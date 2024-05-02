#!/usr/bin/python3
"""
Index file for handling all index related routes for the API.
"""

from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'])
def status():
    """Returns a JSON response with the status of the API."""
    return jsonify({"status": "OK"})
