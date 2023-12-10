from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError

from app.models import Course


class CreateCourseForm(FlaskForm):
    name = StringField("Course", validators=[DataRequired()])
    submit = SubmitField("Submit")

    def validate_name(self, name):
        course = Course.query.filter_by(name=name.data).first()
        if course:
            raise ValidationError("The name has already been taken.")


class UpdateCourseForm(FlaskForm):
    name = StringField("Course", validators=[DataRequired()])
    submit = SubmitField("Submit")
