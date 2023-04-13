from flask import Blueprint

from .math import math_bp
from .joke import joke_bp

api_bp = Blueprint("api", __name__, url_prefix="/api")

api_bp.register_blueprint(joke_bp)
api_bp.register_blueprint(math_bp)


from . import routes