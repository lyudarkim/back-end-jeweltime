from flask import Flask
from flask_cors import CORS
from application.utils.database import setup_db_connection


def create_app(test_config=None):
    app = Flask(__name__)
    CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'

    # Initialize the connection to MongoDB using Flask-PyMongo
    mongodb_client = setup_db_connection(app)

    # Register Blueprints 
    from .modules.accounts.routes import accounts_bp
    from .modules.projects.routes import projects_bp

    app.register_blueprint(accounts_bp)
    app.register_blueprint(projects_bp)

    return app
