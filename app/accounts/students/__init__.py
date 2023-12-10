from flask import Blueprint

blueprint = Blueprint("students", __name__, url_prefix="/students")

from . import views
