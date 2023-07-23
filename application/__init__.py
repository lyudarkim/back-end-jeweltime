from flask import Flask
from flask_pymongo import PyMongo
import os
from dotenv import load_dotenv
from flask_cors import CORS
from application.utils.database import setup_db_connection

load_dotenv()


def create_app(test_config=None):
    app = Flask(__name__)
    CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'

    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    app.config['MONGO_URI'] = os.environ.get('MONGO_URI')

    # Call the setup_db_connection function to set up the database connection
    mongodb_client = setup_db_connection(app)

    # Register Blueprints 
    from .modules.accounts.routes import accounts_bp
    from .modules.projects.routes import projects_bp

    app.register_blueprint(accounts_bp)
    app.register_blueprint(projects_bp)

    return app
