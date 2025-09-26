from app import db


class User(db.Model):
    """Represents a user in the database.

    Attributes:
        id (int): The primary key for the user.
        email (str): The user's email address.
        username (str): The user's username.
        password (str): The user's password.
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, email, password, username):
        """Initializes a new User object.

        Args:
            email (str): The user's email address.
            password (str): The user's password.
            username (str): The user's username.
        """
        self.email = email
        self.password = password
        self.username = username