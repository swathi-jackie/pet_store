from marshmallow import Schema, fields
import random, string
import datetime


def generate_order_id(length=10):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

class product_schema(Schema):
    product_name = fields.String(required=True, allow_none=False)
    product_desc = fields.String(required=True, allow_none=False)
    product_img = fields.String(required=True, allow_none=False)
    price = fields.Integer(required = True, allow_none =False)
    seller_name = fields.String(required=False, allow_none=True)

class order_schema(Schema):
    order_id = fields.UUID(required=True, allow_none=False,default=generate_order_id)  # UUID for order_id
    ordered_on = fields.DateTime(required=True, allow_none=False, default=datetime.datetime.utcnow)  # Automatically sets current date/time if not provided
    payment_mode = fields.String(required=True, allow_none=False)
    purchaser = fields.String(required=False, allow_none=True)  # Purchaser can be optional
    product_name = fields.String(required=True, allow_none=False)