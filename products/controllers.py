from http import HTTPStatus
from bson.objectid import ObjectId
from mongo_functions import MongoFunctions
import settings

class ProductController():
    def __init__(self) -> None:
        self.mongo_functions = MongoFunctions(db=settings.DB_NAME, \
            collection=settings.MONGO_COL_PRODUCTS)
        self.mongo_functions_variants = MongoFunctions(db=settings.DB_NAME, \
            collection=settings.MONGO_COL_VARIANTS)
    
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

    def get_product_by_id(self, product_id):
        return self.mongo_functions.find_one_doc({"_id": ObjectId(product_id)})
    
    def get_all_products_variants(self):
        pipeline = [
            {
                '$group': {
                    '_id': {
                        '$toObjectId': '$product_id'
                    }, 
                    'variants': {
                        '$push': {
                            'id': '$id', 
                            '_id': '$_id', 
                            'variant_name': '$variant_name', 
                            'price': {
                                '$convert': {
                                    'input': '$price', 
                                    'to': 'double'
                                }
                            }
                        }
                    }
                }
            }, {
                '$lookup': {
                    'from': 'products', 
                    'localField': '_id', 
                    'foreignField': '_id', 
                    'as': 'products'
                }
            }, {
                '$addFields': {
                    'product_name': {
                        '$arrayElemAt': [
                            '$products.product_name', 0
                        ]
                    }, 
                    'product_sku': {
                        '$arrayElemAt': [
                            '$products.product_sku', 0
                        ]
                    }
                }
            }, {
                '$sort': {
                    'product_name': 1
                }
            }, {
                '$skip': 1
            }, {
                '$limit': 10
            }, {
                '$project': {
                    'products': 0
                }
            }
        ]
        products_aggregate = list(self.mongo_functions_variants.aggregate_docs(pipeline))
        return products_aggregate, HTTPStatus.OK