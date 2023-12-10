from flask import flash, redirect, render_template, url_for

from app import db
from app.models import Course, Student, User

from . import blueprint
from .forms import StudentCreationForm, StudentUpdateForm


@blueprint.route("/")
def index():
    students = Student.query.all()
    return render_template("students/index.html", students=students)


@blueprint.route("/create", methods=["GET", "POST"])
def create():
    courses = Course.query.all()
    form = StudentCreationForm()
    form.course.choices = [(c.id, c.name) for c in courses]

    if form.validate_on_submit():
        user = User(email=form.email.data, is_student=True)
        user.set_password(form.password.data)

        student = Student(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            course_id=form.course.data,
        )

        user.student = student

        db.session.add_all([user, student])
        db.session.commit()

        flash("Student account created successfully.", "info")
        return redirect(url_for("students.index"))

    return render_template("students/create.html", courses=courses, form=form)


@blueprint.route("/<int:student_id>/edit", methods=["GET", "POST"])
def edit(student_id):
    courses = Course.query.all()
    student = Student.query.get_or_404(int(student_id))
    form = StudentUpdateForm()
    form.course.choices = [(c.id, c.name) for c in courses]

    if form.validate_on_submit():
        # Custom validation to ignore owner email
        # Check if the queried user matches the instructor account.
        # Then check if the provided email is different from the user's email.
        user = User.query.filter_by(email=form.email.data).first()
        if user.id != student.user_id:
            form.email.errors = "Email address is already in use."
        else:
            student.course_id = form.course.data
            student.user.email = form.email.data
            student.first_name = form.first_name.data
            student.last_name = form.last_name.data
            db.session.commit()
            flash("Student information updated successfully.", "info")
            return redirect(url_for("students.index"))

    form.first_name.data = student.first_name
    form.last_name.data = student.last_name
    form.email.data = student.user.email
    form.course.data = student.course_id

    return render_template("students/edit.html", form=form)


@blueprint.post("/<int:student_id>/delete")
def destroy(student_id):
    student = Student.query.get_or_404(int(student_id))
    db.session.delete(student.user)
    db.session.delete(student)
    db.session.commit()

    flash("Student account deleted successfully.", "info")
    return redirect(url_for("students.index"))
