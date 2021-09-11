from mongo_functions import MongoFunctions
import settings


class VariantsController():
    def __init__(self) -> None:
        self.mongo_functions = MongoFunctions(db=settings.DB_NAME,collection=settings.MONGO_COL_VARIANTS)
    