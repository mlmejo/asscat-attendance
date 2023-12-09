import getpass
import secrets

import click
import email_validator

from . import db
from .models import User


@click.command(help="Create a superuser account.")
def create_superuser():
    email = input("Email address: ")
    email_validator.validate_email(email, check_deliverability=False)

    password = getpass.getpass()
    password_confirmation = getpass.getpass("Password (again): ")

    if not secrets.compare_digest(password, password_confirmation):
        raise ValueError("Passwords do not match.")

    user = User(email=email, is_admin=True)
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    click.echo("Superuser created successfully.")
