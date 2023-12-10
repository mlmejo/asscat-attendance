from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, ValidationError

from app.models import Subject


class CreateSubjectForm(FlaskForm):
    descriptive_title = StringField("Descriptive title", validators=[DataRequired()])
    course_number = StringField("Course number", validators=[DataRequired()])
    lec_hours = IntegerField("Lecture hours", validators=[DataRequired()])
    lab_hours = IntegerField("Laboratory hours", validators=[DataRequired()])
    units = IntegerField("Units", validators=[DataRequired()])
    submit = SubmitField("Submit")

    def validate_descriptive_title(self, descriptive_title):
        subject = Subject.query.filter_by(
            descriptive_title=descriptive_title.data
        ).first()
        if subject:
            raise ValidationError("The descriptive title has already been taken.")

    def validate_course_number(self, course_number):
        subject = Subject.query.filter_by(course_number=course_number.data).first()
        if subject:
            raise ValidationError("The course number has already been taken.")


class UpdateSubjectForm(FlaskForm):
    descriptive_title = StringField("Descriptive title", validators=[DataRequired()])
    course_number = StringField("Course number", validators=[DataRequired()])
    lec_hours = IntegerField("Lecture hours", validators=[DataRequired()])
    lab_hours = IntegerField("Laboratory hours", validators=[DataRequired()])
    units = IntegerField("Units", validators=[DataRequired()])
    submit = SubmitField("Update")
