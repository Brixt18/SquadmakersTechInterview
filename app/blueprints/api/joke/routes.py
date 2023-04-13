from flask import abort, make_response, request, url_for

from app.models.models import Joke

from . import joke_bp as bp

@bp.route("/<joke_id>/", methods=["GET"])
def get_by_id(joke_id):
    return make_response({"data": Joke.get_by_id(joke_id, True).joke}, 200)


@bp.route("/", methods=["POST"])
def post():
    joke = request.get_json().get("joke")

    if not joke:
        abort(400, "'joke' field is required.")

    query = Joke(**{"joke": joke})
    query.save(check_auth=False)

    resp = make_response({}, 201)
    resp.headers["Location"] = url_for("api.joke.get_by_id", joke_id=query.id)

    return resp


@bp.route("/", methods=["PATCH"])
def update():
    joke_id = request.args.get("number")

    joke = request.get_json().get("joke")
    query = Joke.get_by_id(joke_id, True)

    if not joke:
        abort(400, "'joke' field is required.")

    query.update({"joke": joke}, check_auth=False)

    return make_response({}, 204)


@bp.route("/", methods=["DELETE"])
def delete():
    joke_id = request.args.get("number")

    query = Joke.get_by_id(joke_id, True)

    query.delete(check_auth=False)

    return make_response({}, 204)
