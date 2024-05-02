#!/usr/bin/python3
"""
Initializes a new blueprint instance for API views.
"""
# Importing all other views modules
from api.v1.views.index import *

from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
