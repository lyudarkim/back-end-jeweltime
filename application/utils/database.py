from flask_pymongo import PyMongo


# Create the PyMongo instance for database connection
mongodb_client = PyMongo()

def setup_db_connection(app):
    # Set up MongoDB with the Flask app
    mongodb_client.init_app(app)

    return mongodb_client  # Return the mongodb_client to the caller (create_app)