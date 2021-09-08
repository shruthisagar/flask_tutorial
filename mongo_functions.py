from pymongo import MongoClient
from pymongo.message import query
import settings

class MongoFunctions:
    def __init__(self, db=None, collection=None):
        # constructor
        if db and collection:
            self.client = MongoClient(host=settings.MONGO_HOST)[db][collection]
        else:
            self.client = MongoClient(host=settings.MONGO_HOST)

    def get_db(self, db_name):
        return self.client[db_name]

    def insert_doc(self, data):
        """

        :param data: data to insert
        :return: inserted_doc
        """
        insert_doc = self.client.insert_one(data)
        return insert_doc

    def find_one_doc(self, query, projection=None):
        find_doc = self.client.find_one(query, projection)
        return find_doc

    def find_many(self, query, projection=None):
        find_doc = self.client.find(query, projection)
        return find_doc

    def update_one_doc(self, query, update_json):
        return self.client.update_one(query, {"$set": update_json})
    
    def aggregate_docs(self, aggregate_pipeline):
        return self.client.aggregate(aggregate_pipeline)
