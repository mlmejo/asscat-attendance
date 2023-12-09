from flask import Blueprint

blueprint = Blueprint("pages", __name__)

from . import views
