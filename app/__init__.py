import os

from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

SECRET_KEY = os.getenv("SECRET_KEY")
if SECRET_KEY is None:
    raise ValueError("Secret key is not provided.")

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
bootstrap = Bootstrap5()


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=SECRET_KEY,
        SQLALCHEMY_DATABASE_URI="sqlite:///database.sqlite",
    )

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    bootstrap.init_app(app)

    from . import accounts, pages
    from .accounts import instructors
    from .main import subjects

    # Project applications
    APPLICATIONS = [
        accounts,
        pages,
        instructors,
        subjects,
    ]

    for _app in APPLICATIONS:
        app.register_blueprint(_app.blueprint)

    from . import commands

    app.cli.add_command(commands.create_superuser)

    return app


from . import models
