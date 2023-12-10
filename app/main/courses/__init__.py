from flask import Blueprint

blueprint = Blueprint("courses", __name__, url_prefix="/courses")

from . import views
