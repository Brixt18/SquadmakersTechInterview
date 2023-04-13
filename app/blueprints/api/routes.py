from flask import abort, redirect, request, url_for

from . import api_bp as bp


@bp.route("/", methods=["GET"])
def get():
    path_param = request.args.get("param", "").lower()

    if (not path_param) or (path_param == "dad"):
        return redirect(url_for("api.joke.dad.get"), code=303)

    elif (path_param == "chuck"):
        return redirect(url_for("api.joke.chuck.get"), code=303)

    else:
        abort(400)
