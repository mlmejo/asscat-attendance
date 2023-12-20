from flask import Blueprint

blueprint = Blueprint(
    "schedules",
    __name__,
    url_prefix="/instructors/<int:instructor_id>/schedules",
)

from . import views
