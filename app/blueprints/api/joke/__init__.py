from flask import Blueprint

from .chucknorris import chucknorris_bp
from .icanhazdadjoke import icanhazdadjoke_bp

joke_bp = Blueprint("joke", __name__)

joke_bp.register_blueprint(chucknorris_bp)
joke_bp.register_blueprint(icanhazdadjoke_bp)

from . import routes