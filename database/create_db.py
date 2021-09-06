import settings
import sys
sys.path.append("..")
from mongo_functions import MongoFunctions
import csv
from random import randint

def generate_org():
    data = {"name": "My Company", "employees": 100}
    MongoFunctions().insert_doc(settings.DB_NAME, settings.MONGO_COL_ORG, data)
    return {"status": 1}

def generate_brands():
    with open('brands.csv', "r") as f:
        csv_data = csv.DictReader(f)
        for i in csv_data:
            MongoFunctions().insert_doc(settings.DB_NAME, settings.MONGO_COL_BRANDS, i)
    return {"status": 1}

def generate_products():
    with open('products.csv',"r") as f:
        csv_data = csv.DictReader(f)
        brand=str(randint(1,10))
        for i in csv_data:
            brand_id = MongoFunctions().find_one_doc(settings.DB_NAME, settings.MONGO_COL_BRANDS, query={"id": brand}, projection={"_id":1})
            i["product_id"] = str(brand_id.get("_id"))
            MongoFunctions().insert_doc(settings.DB_NAME, settings.MONGO_COL_PRODUCTS, i)
    return {"status": 1}

def generate_variants():
    with open('variants.csv',"r") as f:
        csv_data = csv.DictReader(f)
        product_id=str(randint(1,1000))
        for i in csv_data:
            brand_id = MongoFunctions().find_one_doc(settings.DB_NAME, settings.MONGO_COL_PRODUCTS, query={"id": product_id}, projection={"_id":1})
            i["product_id"] = str(brand_id.get("_id"))
            MongoFunctions().insert_doc(settings.DB_NAME, settings.MONGO_COL_PRODUCTS, i)
    return {"status": 1}


if __name__ =="__main__":
    generate_org()
    generate_brands()
    generate_products()
    generate_variants()