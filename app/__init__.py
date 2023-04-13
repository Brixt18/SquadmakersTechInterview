import logging

from flask import Flask, make_response
from flask_models.const import db
from flask_wtf import CSRFProtect
from werkzeug.exceptions import HTTPException

from .configuration.configuration import CONF_MODE

app = Flask(__name__)

csrf = CSRFProtect()
db = db


def configure_logging():
	FORMAT = """[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)s]    %(message)s\n"""
	logging.basicConfig(format=FORMAT)
	logging.disable(logging.INFO)


def create_app():
	app.config.from_object(f"app.configuration.configuration.{CONF_MODE}")
	csrf.init_app(app)
	db.init_app(app)

	from app.blueprints.api import api_bp

	app.register_blueprint(api_bp)

	register_error_handler(app)
	configure_logging()

	return app


def register_error_handler(app):
	@app.errorhandler(Exception)
	def error_handler(e):
		logging.error(f"{type(e).__name__} -> {e}")
		code = 500
		if isinstance(e, HTTPException):
			code = e.code
			if code == 401:
				code = 404

		return make_response({"error": str(e)}, code)
