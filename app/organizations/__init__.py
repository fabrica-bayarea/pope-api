from flask import Blueprint

organizations = Blueprint('organizations', __name__)

from . import views  # noqa
