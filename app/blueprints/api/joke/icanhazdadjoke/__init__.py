from flask import Blueprint

icanhazdadjoke_bp = Blueprint("dad", __name__, url_prefix="/icanhazdadjoke")

from . import routes