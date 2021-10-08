import settings
from mongo_functions import MongoFunctions
from http import HTTPStatus

class UserFunctions():
    def __init__(self) -> None:
        self.mongo_functions = MongoFunctions(db=settings.DB_NAME,collection=settings.MONGO_COL_USERS)
    
    def get_users(self):
        users = list(self.mongo_functions.find_many(query={}, projection={"_id":0}))
        return users

    def insert_user(self, data):
        insert_data = self.mongo_functions.insert_doc(data)
        return {"status": 1}, HTTPStatus.CREATED
    
    def get_user_by_email(self, email, internal=False):
        user = self.mongo_functions.find_one_doc(query={"email": email})
        if internal:
            return user
        return user, HTTPStatus.OK
