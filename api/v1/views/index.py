#!/usr/bin/python3
"""
API Endpoints Index for AirBnB Clone
"""

from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """
    Get the current status of the API.
    Returns:
        JSON: A dictionary containing the API status.
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def number_objects():
    """
    Retrieve the count of each object type in the database.
    Returns:
        JSON: A dictionary with the count of each object type.
    """
    class_map = {
        "amenities": Amenity,
        "cities": City,
        "places": Place,
        "reviews": Review,
        "states": State,
        "users": User
    }

    num_objs = {name: storage.count(cls) for name, cls in class_map.items()}
    return jsonify(num_objs)
