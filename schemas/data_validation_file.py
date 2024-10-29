from flask_restful import reqparse



def non_empty_string(value, name):
    if not value or not value.strip():
        raise ValueError(f"{name} cannot be empty or null.")
    return value


def validate_user_creation_data():
    parser = reqparse.RequestParser()
    parser.add_argument('email',type =non_empty_string,  required=True, help="Email is required.")
    parser.add_argument('password', type =non_empty_string,required=True, help="Password is required.")
    parser.add_argument('first_name',type = non_empty_string, required=True, help="First name is required.")
    parser.add_argument('last_name', type=non_empty_string, required=True, help="Last name is required.")
        
    return parser.parse_args()


def validate_login_values():
    parser = reqparse.RequestParser()
    parser.add_argument('email',type =non_empty_string,  required=True, help="Email is required.")
    parser.add_argument('password', type =non_empty_string,required=True, help="Password is required.")

    return parser.parse_args()

def validate_product_data():
    parser = reqparse.RequestParser()
    parser.add_argument("product_name", type=non_empty_string, required = True, help="product name is required")
    parser.add_argument("product_desc", type=non_empty_string, required = True, help="product desc is required")
    parser.add_argument('product_img', type=str, required=False, help="URL for product image.")
    parser.add_argument('price', type=non_empty_string, required=True, help="Price must be provided and should be an integer.")
    parser.add_argument('seller_email', type=non_empty_string, required=True, help="Seller email cannot be blank and must be valid.")

    return parser.parse_args()