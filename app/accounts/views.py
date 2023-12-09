from flask import render_template, redirect, request
from flask_login import login_user, logout_user

from app.models import User

from . import blueprint
from .forms import LoginForm


@blueprint.route("/", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()
        if user is not None and user.check_password(password):
            login_user(user)
            next_url = request.args.get("next")
            return redirect(next_url) if next_url else redirect("/home")

        form.email.errors = "The provided credentials do not match our records."

    return render_template("welcome.html", form=form)


@blueprint.post("/logout")
def logout():
    logout_user()
    return redirect("/")
