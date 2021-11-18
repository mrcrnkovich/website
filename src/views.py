from flask import Blueprint, flash, render_template, request, session, url_for

bp = Blueprint("views", __name__)


@bp.route("/")
def base_route():
    return render_template("base/base.html")


@bp.route("/about")
def about_route():
    return "Things I know - To Do"


@bp.route("/projects")
def project_route():
    return "List of Projects - To Do"


@bp.route("/contact")
def contact_route():
    return "Contact Me - To Do"
