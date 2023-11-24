from pymongo import MongoClient

client = MongoClient(
    "mongodb://localhost:27017")
db = client.megatronUser

client_admin = MongoClient(
    "mongodb://localhost:27017")
db_admin = client_admin.megatronDB

class mongo_connection:

    def db_connection(self):
        return db, db_admin