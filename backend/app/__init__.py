import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
"""The database object."""

migrate = Migrate()
"""The database migration object."""

def create_app():
    """Creates and configures the Flask application.

    Returns:
        The Flask application.
    """
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://" + os.environ.get('DB_USER') + ":" + os.environ.get('DB_PASSWORD') + "@" + os.environ.get('DB_HOST') + "/" + os.environ.get('DB_NAME')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    migrate.init_app(app, db)

    from .models import user

    from .views import root_bp, authenticate_bp
    
    app.register_blueprint(root_bp, url_prefix='/')
    app.register_blueprint(authenticate_bp)


    return app