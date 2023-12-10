from flask_wtf import FlaskForm
from wtforms import (EmailField, PasswordField, SelectField, StringField,
                     SubmitField)
from wtforms.validators import DataRequired, ValidationError

from app.models import Course, User


class StudentCreationForm(FlaskForm):
    course = SelectField("Course", coerce=int)
    first_name = StringField("First name", validators=[DataRequired()])
    last_name = StringField("Last name", validators=[DataRequired()])
    email = EmailField("Email adddress", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")


    def validate_course(self, course):
        course = Course.query.filter_by(id=course.data).first()
        if not course:
            raise ValidationError("Course does not exist.")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("The email address has already been taken.")


class StudentUpdateForm(FlaskForm):
    course = SelectField("Course", coerce=int)
    first_name = StringField("First name", validators=[DataRequired()])
    last_name = StringField("Last name", validators=[DataRequired()])
    email = EmailField("Email adddress", validators=[DataRequired()])
    submit = SubmitField("Submit")

    def validate_course(self, course):
        course = Course.query.filter_by(id=course.data).first()
        if not course:
            raise ValidationError("Course does not exist.")
