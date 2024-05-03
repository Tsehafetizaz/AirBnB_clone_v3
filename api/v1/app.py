#!/usr/bin/python3
"""
Flask Application for AirBnB Clone API
"""

from flask import Flask, jsonify, make_response
from flask_cors import CORS
from flasgger import Swagger
from os import environ
from models import storage
from api.v1.views import app_views

# Initialize Flask application
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['SWAGGER'] = {
    'title': 'AirBnB Clone Restful API',
    'uiversion': 3
}
app.register_blueprint(app_views)

# Configure CORS for the app
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})

# Initialize Swagger documentation
Swagger(app)

@app.teardown_appcontext
def close_db(error):
    """
    Close the database session at the end of the request
    """
    storage.close()

@app.errorhandler(404)
def not_found(error):
    """
    Custom error handler for 404 errors.
    ---
    responses:
      404:
        description: The requested resource was not found.
    """
    return make_response(jsonify({'error': "Not found"}), 404)

if __name__ == "__main__":
    # Main entry for running the Flask application
    host = environ.get('HBNB_API_HOST', '0.0.0.0')
    port = environ.get('HBNB_API_PORT', '5000')
    app.run(host=host, port=port, threaded=True)

