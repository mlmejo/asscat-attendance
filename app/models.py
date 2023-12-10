from flask_login import UserMixin
from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Boolean, Enum, Integer, String, Text
from werkzeug.security import check_password_hash, generate_password_hash

from app import db, login_manager
from app.enums import YearLevelChoices


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(Text, nullable=False)
    is_admin = Column(Boolean, default=False)
    is_instructor = Column(Boolean, default=False)
    is_student = Column(Boolean, default=False)

    # Relationships
    instructor = db.relationship(
        "Instructor",
        backref="user",
        uselist=False,
        lazy=True,
        cascade="all, delete",
    )
    student = db.relationship(
        "Student",
        backref="user",
        uselist=False,
        lazy=True,
        cascade="all, delete",
    )

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def set_password(self, password):
        self.password = generate_password_hash(password)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Subject(db.Model):
    id = Column(Integer, primary_key=True)
    descriptive_title = Column(String(64), unique=True, nullable=False)
    course_number = Column(String(32), unique=True, nullable=False)
    lec_hours = Column(Integer, nullable=False)
    lab_hours = Column(Integer, nullable=False)
    units = Column(Integer, nullable=False)


class Instructor(db.Model):
    id = Column(Integer, primary_key=True)
    first_name = Column(String(64), nullable=False)
    last_name = Column(String(64), nullable=False)
    user_id = Column(
        Integer,
        ForeignKey("user.id"),
        unique=True,
        nullable=False,
    )


class Course(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True, nullable=False)

    # Relationships
    students = db.relationship(
        "Student",
        backref="course",
        lazy=True,
        cascade="all, delete",
    )


class Student(db.Model):
    id = Column(Integer, primary_key=True)
    first_name = Column(String(64), nullable=False)
    last_name = Column(String(64), nullable=False)
    year_level = Column(Enum(YearLevelChoices))
    user_id = Column(
        Integer,
        ForeignKey("user.id"),
        unique=True,
        nullable=False,
    )
    course_id = Column(Integer, ForeignKey("course.id"), nullable=False)


class InstructorLoad(db.Model):
    id = Column(Integer, primary_key=True)
    school_year = Column(String(64), nullable=False)
    start_time = Column(String(64), nullable=False)
    day = Column(String(64), nullable=False)
    end_time = Column(String(64), nullable=False)
    instructor_id = Column(Integer, ForeignKey("instructor.id"), nullable=False)
    subject_id = Column(Integer, ForeignKey("subject.id"), nullable=False)

    instructor = db.relationship("Instructor", back_populates="load", lazy=True)
    subject = db.relationship("Subject", lazy=True)
