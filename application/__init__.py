from flask import Flask
from flask_cors import CORS
import logging
from application.utils.database import setup_db_connection


def configure_logging(app):
    if app.debug:
        # In development mode, log all messages, including lower-severity ones
        logging_level = logging.DEBUG 
    else:
        # In production, log only important messages for better clarity
        logging_level = logging.INFO

    # Capture routine operations and above from Flask's internal server (Werkzeug)
    werkzeug_log_level = logging.INFO  

    # Set the format for displaying logs
    logging.basicConfig(level=logging_level, 
                        format='\n%(asctime)s %(levelname)s: \n%(message)s \n[in %(pathname)s:%(lineno)d]')

    # Set Werkzeug log level
    logging.getLogger('werkzeug').setLevel(werkzeug_log_level)


# Remove testing=True argument when in production
def create_app(testing=True):
    app = Flask(__name__)
    CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'

    # Initialize the connection to MongoDB using Flask-PyMongo
    setup_db_connection(app, testing)

    # Register Blueprints 
    from .modules.accounts.routes import accounts_bp
    from .modules.projects.routes import projects_bp
    from .modules.projects.routes import get_all_projects_bp

    app.register_blueprint(accounts_bp)
    app.register_blueprint(projects_bp)
    app.register_blueprint(get_all_projects_bp)

    # Set up logging
    configure_logging(app)  

    return app
