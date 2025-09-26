from flask import Blueprint

root_bp = Blueprint('root_bp', __name__)


@root_bp.route("/")
def home():
    """The root endpoint.

    Returns:
        A string indicating that the service is running.
    """
    return "Flask Service running"
