from flask import Flask
from flask_cors import CORS
from application.utils.database import setup_db_connection


# Remove testing=True argument when in production
def create_app(testing=True):
    app = Flask(__name__)
    CORS(app, origins=['http://localhost:3001'])
    app.config['CORS_HEADERS'] = 'Content-Type'

    # Initialize the connection to MongoDB using Flask-PyMongo
    setup_db_connection(app, testing)

    # Register Blueprints 
    from .modules.accounts.routes import accounts_bp, signin_bp
    from .modules.projects.routes import projects_bp, get_all_projects_bp
    from .modules.metals.routes import metals_bp

    app.register_blueprint(accounts_bp)
    app.register_blueprint(signin_bp)
    app.register_blueprint(projects_bp)
    app.register_blueprint(get_all_projects_bp)
    app.register_blueprint(metals_bp)

    return app
