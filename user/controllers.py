import settings
from mongo_functions import MongoFunctions

class UserFunctions():
    def __init__(self) -> None:
        self.mongo_functions = MongoFunctions()
    
    def get_users(self):
        users = self.mongo_functions.find_one_doc(settings.DB_NAME, settings.MONGO_COL_PRODUCTS, {}, projection={"_id":0})
        return users
