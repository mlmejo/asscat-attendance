from flask import render_template
from flask_login import current_user, login_required

from . import blueprint


@blueprint.route("/home")
@login_required
def home():
    if current_user.is_admin:
        return render_template("admin/dashboard.html")
