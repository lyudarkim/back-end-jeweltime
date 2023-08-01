import os
from dotenv import load_dotenv
from pymongo import MongoClient
import certifi

# THIS FILE IS FOR TESTING THE CONNECTION TO THE DB AND TESTING DB
# Delete after finishing the project

load_dotenv()
MONGODB_TEST_URI = os.environ.get('MONGODB_TEST_URI')
# MONGODB_URI = os.environ.get('MONGODB_URI')

# Need this 2nd argument, otherwise you get the 'pymongo [SSL: CERTIFICATE_VERIFY_FAILED]' error
client = MongoClient(MONGODB_TEST_URI, tlsCAFile=certifi.where())

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# for db_name in client.list_database_names():
#     print(db_name)

# client.close()