from flask_sqlalchemy import SQLAlchemy
import datetime


db= SQLAlchemy()

class Product(db.Model):
    __tablename__ = 'product'
    product_name = db.Column(db.String(200), primary_key=True)
    product_desc = db.Column(db.String(1000), nullable=False)
    product_img = db.Column(db.String(100), nullable = True)
    price = db.Column(db.Integer, nullable = True)
    seller_name = db.Column(db.String(200), nullable= True)
    orders =db.relationship('Order', backref='product')

class Order(db.Model):
    __tablename__='orders'
    order_id = db.Column(db.String(50), primary_key=True)# this id needs to be autogenerated once user completes purchase
    ordered_on = db.Column(db.DateTime(), nullable=False)
    payment_mode = db.Column(db.String(50), nullable = False)
    purchaser = db.Column(db.String(200), nullable=True)
    product_name = db.Column(db.String(200), db.ForeignKey('product.product_name'), nullable=True)
    review =  db.Column(db.String(5000), nullable = True)

class Seller(db.Model):
    __tablename__='Sellers'
    username = db.Column(db.String(50), primary_key=True)
    password = db.Column(db.String(50), nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)



     







    
