from flask import Blueprint

blueprint = Blueprint("subjects", __name__, url_prefix="/subjects")

from . import views
