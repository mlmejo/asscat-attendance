from flask import flash, redirect, render_template, url_for
from sqlalchemy.exc import IntegrityError

from app import db
from app.models import Instructor, User

from . import blueprint
from .forms import InstructorCreationForm, InstructorUpdateForm


@blueprint.route("/")
def index():
    instructors = Instructor.query.all()
    return render_template("instructors/index.html", instructors=instructors)


@blueprint.route("/create", methods=["GET", "POST"])
def create():
    form = InstructorCreationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data, is_instructor=True)
        user.set_password(form.password.data)

        instructor = Instructor(
            first_name=form.first_name.data, last_name=form.last_name.data
        )

        user.instructor = instructor

        db.session.add_all([user, instructor])
        db.session.commit()

        flash("Instructor added successfully.", "info")
        return redirect(url_for("instructors.index"))

    return render_template("instructors/create.html", form=form)


@blueprint.route("/<int:instructor_id>/edit", methods=["GET", "POST"])
def edit(instructor_id):
    instructor = Instructor.query.get_or_404(int(instructor_id))
    form = InstructorUpdateForm()

    if form.validate_on_submit():
        # Custom validation to ignore owner email
        # Check if the queried user matches the instructor account.
        # Then check if the provided email is different from the user's email.
        user = User.query.filter_by(email=form.email.data).first()
        if user.id != instructor.user_id:
            form.email.errors = "Email address is already in use."
        else:
            instructor.user.email = form.email.data
            instructor.first_name = form.first_name.data
            instructor.last_name = form.last_name.data
            db.session.commit()
            flash("Instructor information updated successfully.", "info")
            return redirect(url_for("instructors.index"))

    form.first_name.data = instructor.first_name
    form.last_name.data = instructor.last_name
    form.email.data = instructor.user.email

    return render_template("instructors/edit.html", form=form)


@blueprint.post("/<int:instructor_id>/delete")
def destroy(instructor_id):
    instructor = Instructor.query.get_or_404(int(instructor_id))
    db.session.delete(instructor.user)
    db.session.delete(instructor)
    db.session.commit()

    flash("Instructor account deleted successfully.", "info")

    return redirect(url_for("instructors.index"))
