from flask import flash, redirect, render_template, url_for

from app import db
from app.models import Course

from . import blueprint
from .forms import CreateCourseForm, UpdateCourseForm


@blueprint.route("/")
def index():
    courses = Course.query.all()
    return render_template("courses/index.html", courses=courses)


@blueprint.route("/create", methods=["GET", "POST"])
def create():
    form = CreateCourseForm()

    if form.validate_on_submit():
        course = Course(name=form.name.data)

        db.session.add(course)
        db.session.commit()

        flash("Course created successfully.", "info")
        return redirect(url_for("courses.index"))

    return render_template("courses/create.html", form=form)


@blueprint.route("/<int:course_id>/edit", methods=["GET", "POST"])
def edit(course_id):
    course = Course.query.get(int(course_id))
    form = UpdateCourseForm(obj=course)

    if form.validate_on_submit():
        _course = Course.query.filter_by(name=form.name.data).first()
        if _course and _course.name != course.name:
            form.name.errors = "The name has already been taken."

        course.name = form.name.data
        db.session.commit()

        flash("Course updated successfully.", "info")
        return redirect(url_for("courses.index"))

    return render_template("courses/edit.html", form=form)


@blueprint.post("/<int:course_id>/delete")
def destroy(course_id):
    course = Course.query.get(int(course_id))
    db.session.delete(course)
    db.session.commit()

    flash("Course deleted successfully.", "info")
    return redirect(url_for("courses.index"))
