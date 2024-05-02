#!/usr/bin/python3
"""
API script that initializes Flask app and includes all configurations,
including CORS, blueprints, and error handling.
"""

from flask import Flask, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views
from os import getenv


def create_app():
    """
    Initializes the Flask application, configures it, and registers components.
    Returns the configured app instance.
    """
    app = Flask(__name__)
    configure_app(app)
    register_blueprints(app)
    register_teardowns(app)
    setup_cors(app)
    register_error_handlers(app)
    return app


def configure_app(app):
    """ Configure the Flask app with environment-specific settings. """
    pass  # Future configurations could be placed here.


def register_blueprints(app):
    """ Registers all blueprints for the application. """
    app.register_blueprint(app_views)


def register_teardowns(app):
    """
    Register teardown app context actions.
    """
    @app.teardown_appcontext
    def teardown_appcontext(exception=None):
        """ Closes storage after app context is destroyed. """
        storage.close()


def setup_cors(app):
    """ Sets up Cross-Origin Resource Sharing for the app. """
    origins = getenv('CORS_ORIGINS', '0.0.0.0')
    CORS(app, origins=origins)


def register_error_handlers(app):
    """
    Register error handlers for the application.
    """
    @app.errorhandler(404)
    def page_not_found(error):
        """ Returns a custom JSON response for 404 errors. """
        return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    app = create_app()
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = getenv('HBNB_API_PORT', '5000')
    app.run(host=host, port=port, threaded=True)
