from flask import flash, redirect, render_template, url_for

from app import db
from app.models import Subject

from . import blueprint
from .forms import CreateSubjectForm, UpdateSubjectForm


@blueprint.route("/")
def index():
    subjects = Subject.query.all()
    return render_template("subjects/index.html", subjects=subjects)


@blueprint.route("/create", methods=["GET", "POST"])
def create():
    form = CreateSubjectForm()

    if form.validate_on_submit():
        subject = Subject(
            descriptive_title=form.descriptive_title.data,
            course_number=form.course_number.data,
            lec_hours=form.lec_hours.data,
            lab_hours=form.lab_hours.data,
            units=form.units.data,
        )

        db.session.add(subject)
        db.session.commit()

        flash("Subject created successfully.", "info")
        return redirect(url_for("subjects.index"))

    return render_template("subjects/create.html", form=form)


@blueprint.route("/<int:subject_id>/edit", methods=["GET", "POST"])
def edit(subject_id):
    subject = Subject.query.get_or_404(subject_id)
    form = UpdateSubjectForm(obj=subject)

    if form.validate_on_submit():
        subject.descriptive_title = form.descriptive_title.data
        subject.course_number = form.course_number.data
        subject.lec_hours = form.lec_hours.data
        subject.lab_hours = form.lab_hours.data
        subject.units = form.units.data

        db.session.commit()

        flash("Subject updated successfully.", "info")
        return redirect(url_for("subjects.index"))

    return render_template("subjects/edit.html", form=form)


@blueprint.post("/<int:subject_id>/delete")
def destroy(subject_id):
    subject = Subject.query.get_or_404(subject_id)

    db.session.delete(subject)
    db.session.commit()

    flash("Subject deleted successfully.", "info")

    return redirect(url_for("subjects.index"))
