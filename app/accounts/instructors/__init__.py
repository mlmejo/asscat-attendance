from flask import Blueprint

blueprint = Blueprint("instructors", __name__, url_prefix="/instructors")

from . import views
