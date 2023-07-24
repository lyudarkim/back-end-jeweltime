import os
import certifi
import urllib.parse
from dotenv import load_dotenv
from flask_pymongo import PyMongo


load_dotenv()

# Encode the path to the certificate we get from certifi.where()
cert_path = urllib.parse.quote_plus(certifi.where())

MONGO_URI = os.environ.get('MONGO_URI')
# Append the encoded tlsCAFile param to the MongoDB URI
# Without it, the 'pymongo [SSL: CERTIFICATE_VERIFY_FAILED]' error occurs
MONGO_URI += f"?tlsCAFile={cert_path}"

# Create an instance of Flask-PyMongo which we will initialize later 
pymongo = PyMongo()


def setup_db_connection(app):
    """
    This function sets up the connection to MongoDB using Flask-PyMongo
    """
    app.config['MONGO_URI'] = MONGO_URI
    pymongo.init_app(app)

    return pymongo  


