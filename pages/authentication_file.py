from flask_restful import Resource, request, reqparse
from models.tables import Seller
from flask import make_response
from models.tables import db
from schemas.data_validation_file import validate_user_creation_data as validate_payload
from schemas.data_validation_file import validate_login_values
from werkzeug.security import check_password_hash, generate_password_hash
import uuid
from datetime import datetime, timedelta


class userAuthentication(Resource):
    def post(self):
        data = validate_payload()
        email = data['email']
        password = data['password']
        first_name = data['first_name']
        last_name = data['last_name']

        if email and password and first_name and last_name:
            user = Seller.query.filter_by(email=email).first()
            if user:
                return make_response({"message":"Account already exists please sign in:)"},200)
            else:
                seller = Seller(
                    email= email,
                    password= generate_password_hash(password),
                    first_name=first_name,
                    last_name= last_name
                )
                db.session.add(seller)
                db.session.commit()
                return make_response({"message":"User created Successfully"},201)
            

class Login(Resource):
    def post(self):
        data = validate_login_values()
        email = data['email']
        password = data['password']

        user = Seller.query.filter_by(email = email).first()
        if not user:
            return make_response({"message":"please create your account"}, 401)
        if check_password_hash(user.password, password):
            id = uuid.uuid4().hex
            exp = datetime.utcnow()+timedelta(minutes=30)
            return make_response(
                {
                    "access_token":id,
                    "exp":exp
                },
                200
            )
        
        else:
            return make_response({"message":"check the credentials"}, 401)
        
            
        


