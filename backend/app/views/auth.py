from flask import request
from flask_restful import Resource
from werkzeug.security import generate_password_hash
from app.models.user import User
from app import db
from cerberus import Validator


class Register(Resource):
    """Handles user registration."""
    class InputValidator(Validator):
        """Validator for the registration input.

        Attributes:
            schema (dict): The validation schema.
            rules (dict): The validation rules.
        """
        def __init__(self):
            """Initializes the validator with the registration schema."""
            super().__init__()
            self.schema = {
                'email': {'type': 'string', 'required': True, 'unique_email': True},
                'password': {'type': 'string', 'required': True},
                'username': {'type': 'string', 'required': True}
            }
            self.rules.update({'unique_email': self._validate_unique_email})

        def _validate_unique_email(self, constraint, field, value):
            """Validates that the email is unique.

            Args:
                constraint (bool): The constraint value from the schema.
                field (str): The name of the field being validated.
                value (str): The value of the field being validated.
            """
            if constraint and User.query.filter_by(email=value).first():
                self._error(field, 'User with that email already exists')
    
    def post(self):
        """Creates a new user.

        The user's details are extracted from the JSON body of the request.

        Returns:
            A tuple containing a dictionary and an HTTP status code. The dictionary
            will either contain a success message and the new user's ID, or an
            error message.
        """

        validator = Register.InputValidator({
            'email': {'type': 'string', 'required': True, 'unique_email': True},
            'password': {'type': 'string', 'required': True},
            'username': {'type': 'string', 'required': True}
        })

        if not validator.validate(request.json):
            return {'message': 'Invalid request data', 'errors': validator.errors}, 400
        email = request.json.get('email')
        password = request.json.get('password')
        username = request.json.get('username')    

        hashed_password = generate_password_hash(password, method='sha256')

        try:
            user = User(
                email=email, 
                username=username, 
                password=hashed_password
            )
            db.session.add(user)
            db.session.commit()
        except Exception:
            return {'message': 'An unexpected error occured'}, 500

        return {'message': 'Resource created successfully.',
                'id': user.id}, 201

class Login(Resource):
    """Handles user login."""
    def post(self):
        """Logs a user in.

        The user's credentials are extracted from the JSON body of the request.

        Returns:
            A dictionary with the login status.
        """
        email = request.json.get('email')
        password = request.json.get('password')

        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            return {'status': 'success'}
        else:
            return {'status': 'error'}