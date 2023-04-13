from flask import Blueprint

chucknorris_bp = Blueprint("chuck", __name__, url_prefix="/chucknorris")

from . import routes