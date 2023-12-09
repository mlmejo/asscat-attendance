from flask import Blueprint

blueprint = Blueprint("accounts", __name__)

from . import views
