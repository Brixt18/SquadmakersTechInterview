from os import getcwd, getenv
from os.path import abspath

from dotenv import load_dotenv

# Load enviroment vars from .env file. If the file is not being read correctly, that must be because of a path error.
# I.E: load_dotenv("/var/www/myapp/.env")
load_dotenv()

CONF_MODE = getenv("CONF_MODE")


class Config(object):
	SECRET_KEY = getenv("SECRET_KEY")
	PATH = getenv("PROJECT_PATH", abspath(getcwd()))

	# CONFIGURATION FLASK
	# https://flask.palletsprojects.com/en/0.12.x/config/
	SESSION_COOKIE_SECURE = True
	SESSION_COOKIE_HTTPONLY = True
	SESSION_COOKIE_SAMESITE = 'Lax'
	SERVER_NAME = getenv("SERVER_NAME")

	# CONFIGURATION FLASK-WTF
	# https://flask-wtf.readthedocs.io/en/1.0.x/config/
	WTF_CSRF_ENABLED = False

	# CONFIGURATION FLASK-SQLALCHEMY
	# https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/config/
	SQLALCHEMY_DATABASE_URI = f"sqlite:///{PATH}/.database.db"
	SQLALCHEMY_TRACK_MODIFICATIONS = False


class Production(Config):
	DEBUG = False


class Development(Config):
	DEBUG = True


class Local(Config):
	DEBUG = True
	SESSION_COOKIE_SECURE = False
