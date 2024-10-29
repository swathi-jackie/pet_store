import random
from flask_restful import Resource
from models.tables import db
from schemas import schemas
from models.tables import Product as ProductModel, db
from flask import make_response, jsonify
from schemas.data_validation_file import validate_product_data 



def generate_product_id():
    # while True:
    pid = random.randint(1000, 2147483647)
    if not ProductModel.query.filter_by(pid=pid).first():
        return pid 
    
class ProductResource(Resource):
    def get(self, pid = None):
        product_schema = schemas.product_schema()
        if pid:
            result = ProductModel.query.get(pid)
            if result is not None:
                res = product_schema.dump(result)
                return make_response({"message":res},200)
            else:
                return make_response({"message":"the product is not found"},202)
            
    def post(self):
        data=validate_product_data()
        pid=generate_product_id(),
        new_product = ProductModel(
            pid=pid,
            product_name=data['product_name'],
            product_desc=data['product_desc'],
            product_img=data['product_img'],
            price=data['price'],
            seller_email=data['seller_email']
        )
        db.session.add(new_product)
        db.session.commit()
        return make_response({"message":"Product created Successfully","product_id":pid}, 201)