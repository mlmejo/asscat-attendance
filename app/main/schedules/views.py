from flask import render_template

from app.models import Course, Instructor, Subject

from . import blueprint


@blueprint.route("")
def index(instructor_id: int):
    instructor = Instructor.query.get_or_404(instructor_id)
    courses = Course.query.all()
    subjects = Subject.query.all()

    return render_template(
        "schedules/index.html",
        instructor=instructor,
        courses=courses,
        subjects=subjects,
    )
