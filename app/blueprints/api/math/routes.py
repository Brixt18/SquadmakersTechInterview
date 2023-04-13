from math import lcm

from flask import make_response, request

from . import math_bp as bp


@bp.route("/least-common-multiple/", methods=["GET"])
def least_common_multiple():
    numbers = request.args.get("numbers", "").split(",")
    numbers = tuple((int(n) for n in numbers if n.isdigit()))

    return make_response({"data": lcm(*numbers)}, 200)


@bp.route("/add-one/", methods=["GET"])
def add_one():
    return make_response({"data": f"{(request.args.get('number', -1, type=int))+1}"}, 200)
