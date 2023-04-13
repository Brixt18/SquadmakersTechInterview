from flask_models.const import *
from flask_models.models import Model


class Joke(Model):
    joke = COLUMN(STRING, nullable=False)
