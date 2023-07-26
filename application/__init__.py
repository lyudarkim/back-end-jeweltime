from flask import Flask
from flask_cors import CORS
from application.utils.database import setup_db_connection


def create_app(test_config=None):
    app = Flask(__name__)
    CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'

    # Use test_config to determine which database to connect to
    testing = False
    if test_config:
        testing = True

    # Initialize the connection to MongoDB using Flask-PyMongo
    mongodb_client = setup_db_connection(app, testing)

    # Register Blueprints 
    from .modules.accounts.routes import accounts_bp
    from .modules.projects.routes import projects_bp

    app.register_blueprint(accounts_bp)
    app.register_blueprint(projects_bp)

    return app
