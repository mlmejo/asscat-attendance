from flask import render_template

from app.models import Course, Subject

from . import blueprint


@blueprint.route("/")
def index():
    courses = Course.query.all()
    subjects = Subject.query.all()

    return render_template(
        "schedules/index.html",
        courses=courses,
        subjects=subjects,
    )
