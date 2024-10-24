import datetime
import random, string
from flask_restful import Api, Resource
from schemas import schemas
from models.tables import Orders as OrderModel
from flask import jsonify, request
from models.tables import db


def generate_order_id(length=10):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def generate_unique_order_id():
    """Generate a unique 10-digit integer order ID."""
    while True:
        order_id = random.randint(1000000000, 9999999999)
        if not OrderModel.query.filter_by(order_id=order_id).first():
            return order_id  # Return if the ID does not exist


class OrderResource(Resource):

    order_detail = schemas.order_schema()
    order_details = schemas.order_schema(many=True)
    def get(self, order_id: str = None):
        if order_id:
            order = OrderModel.query.get(order_id)
            if order is None:
                return {"message":"Order Not found"}, 400
            else:
                return {"response":self.order_detail.dump(order)}, 200
        else:
            orders = OrderModel.query.all()
            result = self.order_details.dump(orders)
            return {"result":result},200
        

    def post(self):
        data = request.get_json()
        # validating fields
        errors = {}
        if 'payment_mode' not in data:
            errors['payment_mode'] = 'Payment mode is required.'
        if 'product_name' not in data:
            errors['product_name'] = 'Product name is required.'
        
        if errors:
            return {"errors": errors}, 400
        
        # Create a new Order instance
        new_order = OrderModel(
            order_id= generate_order_id(), # Generate a new unique order ID
            ordered_on= datetime.datetime.now().strftime('%Y-%m-%d'),  #current date
            payment_mode=data['payment_mode'],
            purchaser=data.get('purchaser'),  #optional fields
            product_name=data['product_name'],
            review=data.get('review')  # Optional field
        )

        result = db.session.execute('select A.order_id,B.product_name,B.price,A.ordered_on from orders as A INNER JOIN products as B where A.product_name=B.product_name').first()
        db.session.add(new_order)
        db.session.commit()

        return {"response": {"order_id": new_order.order_id}}, 201

    

