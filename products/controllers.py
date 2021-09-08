from mongo_functions import MongoFunctions
import settings

class ProductController():
    def __init__(self) -> None:
        self.mongo_functions = MongoFunctions(db=settings.DB_NAME, \
            collection=settings.MONGO_COL_PRODUCTS)
    
    def get_products(self, request_args):
        skip = int(request_args.get("skip", 0))
        limit = int(request_args.get("limit", 10))
        search_key = request_args.get("search_key", "")
        # products_list_mongo  = list(self.mongo_functions.find_many({"id":"1"}))
        products_search_pipeline = [
            {
                '$match': {
                    'product_name': {
                        '$regex': search_key,
                        '$options': 'si'
                    }
                }
            }, {
                '$skip': skip
            }, {
                '$limit': limit
            }
        ]
        products_aggregate = list(self.mongo_functions.aggregate_docs(products_search_pipeline))
        return products_aggregate
        # return products_list_mongo

