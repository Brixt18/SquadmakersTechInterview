from flask import abort, make_response
from requests import get as r_get

from . import chucknorris_bp as bp


@bp.route("/", methods=["GET"])
def get():
    joke = r_get("https://api.chucknorris.io/jokes/random",
                 headers={"Accept": "application/json"}).json().get("value")

    if not joke:
        abort(500, "The chuck norris api did not return a valid value")

    return make_response({"data": joke}, 200)
