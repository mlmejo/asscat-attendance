from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class CreateSubjectForm(FlaskForm):
    descriptive_title = StringField("Descriptive title", validators=[DataRequired()])
    course_number = StringField("Course number", validators=[DataRequired()])
    lec_hours = IntegerField("Lecture hours", validators=[DataRequired()])
    lab_hours = IntegerField("Laboratory hours", validators=[DataRequired()])
    units = IntegerField("Units", validators=[DataRequired()])
    submit = SubmitField("Submit")


class UpdateSubjectForm(FlaskForm):
    descriptive_title = StringField("Descriptive title", validators=[DataRequired()])
    course_number = StringField("Course number", validators=[DataRequired()])
    lec_hours = IntegerField("Lecture hours", validators=[DataRequired()])
    lab_hours = IntegerField("Laboratory hours", validators=[DataRequired()])
    units = IntegerField("Units", validators=[DataRequired()])
    submit = SubmitField("Update")
