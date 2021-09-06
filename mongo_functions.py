from pymongo import MongoClient
import settings

class MongoFunctions:
    def __init__(self):
        # constructor
        self.client = MongoClient(host=settings.MONGO_HOST)

    def get_db(self, db_name):
        return self.client[db_name]

    def insert_doc(self, db_name, collection, data):
        """

        :param db_name: database name
        :param collection: collection name
        :param data: data to insert
        :return:
        """
        db = self.get_db(db_name)
        insert_doc = db[collection].insert_one(data)
        return insert_doc

    def find_one_doc(self, db_name, collection, query, projection=None):
        db = self.get_db(db_name)
        find_doc = db[collection].find_one(query, projection)
        return find_doc

    def update_one_doc(self, db_name, collection, query, update_json):
        db = self.get_db(db_name)
        return db[collection].update_one(query, {"$set": update_json})
    
    # def 
