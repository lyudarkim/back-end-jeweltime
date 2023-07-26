import os
import certifi
import urllib.parse
from dotenv import load_dotenv
from flask_pymongo import PyMongo


load_dotenv()

# Encode the path to the certificate we get from certifi.where()
cert_path = urllib.parse.quote_plus(certifi.where())

MONGODB_TEST_URI = os.environ.get('MONGODB_TEST_URI')
MONGODB_URI = os.environ.get('MONGODB_URI')

if not MONGODB_URI:
    raise ValueError("MONGODB_URI is not set in the environment or .env file")


# Get the correct database URI
def get_db_uri(testing=False):
    uri = MONGODB_TEST_URI if testing else MONGODB_URI

    # Append the encoded tlsCAFile param to the URI
    # Without it, the 'pymongo [SSL: CERTIFICATE_VERIFY_FAILED]' error occurs
    cert_path = urllib.parse.quote_plus(certifi.where())
    uri += f"?tlsCAFile={cert_path}"
    return uri

# MONGODB_URI += f"?tlsCAFile={cert_path}"

# Create an instance of Flask-PyMongo which we will initialize later 
pymongo = PyMongo()


def setup_db_connection(app, testing=False):
    """
    This function sets up the connection to MongoDB using Flask-PyMongo
    """
    app.config['MONGO_URI'] = get_db_uri(testing)
    pymongo.init_app(app)

    return pymongo  


