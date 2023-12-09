from flask_login import UserMixin
from sqlalchemy import Column
from sqlalchemy.types import Boolean, Integer, String, Text
from werkzeug.security import check_password_hash, generate_password_hash

from app import db, login_manager


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(Text, nullable=False)
    is_admin = Column(Boolean, default=False)

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
