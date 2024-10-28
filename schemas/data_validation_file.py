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

