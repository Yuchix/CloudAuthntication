from flask import Blueprint, render_template
from flask_jwt_extended import jwt_required, get_jwt_identity

main_bp = Blueprint('main', __name__)

@main_bp.route("/")
@jwt_required(locations=["cookies"])  # Tell Flask-JWT-Extended to read JWT from cookies
def home():
    username = get_jwt_identity()
    return render_template("home.html", username=username)
