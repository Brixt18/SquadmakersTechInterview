from flask import abort, make_response
from requests import get as r_get

from . import icanhazdadjoke_bp as bp


@bp.route("/", methods=["GET"])
def get():
    joke = r_get("https://icanhazdadjoke.com/",
                 headers={"Accept": "application/json"}).json().get("joke")

    if not joke:
        abort(500, "The icannhazdadjoke api did not return a valid value")

    return make_response({"data": joke}, 200)
