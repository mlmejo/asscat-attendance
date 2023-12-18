from flask import Blueprint

blueprint = Blueprint("schedules", __name__, url_prefix="/schedules")

from . import views
