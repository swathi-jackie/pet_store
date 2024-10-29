from flask import Flask
from models.tables import db
from flask_migrate import Migrate
from flask_restful import Api
from pages import orders, authentication_file as User, products as Product


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://<username>:<password>@localhost:5432/PetStore_new'
db.init_app(app)
migrate = Migrate(app,db)


api = Api(app)

api.add_resource(orders.OrderResource, "/orders","/orders/<order_id>")
api.add_resource(User.userAuthentication,"/signup")
api.add_resource(User.Login, "/login")
api.add_resource(Product.ProductResource, "/product","/product/<pid>")

if __name__ == '__main__':
    app.run(debug=True)

