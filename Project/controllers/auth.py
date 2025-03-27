from flask import Blueprint, request, render_template, redirect, url_for, make_response
from flask_jwt_extended import create_access_token, set_access_cookies
from datetime import timedelta

auth_bp = Blueprint('auth', __name__)

# Dummy User
VALID_USER = {"username": "admin", "password": "password123"}

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == VALID_USER["username"] and password == VALID_USER["password"]:
            access_token = create_access_token(identity=username, expires_delta=timedelta(hours=1))
            response = make_response(redirect(url_for("main.home")))
            set_access_cookies(response, access_token)
            return response  # Ensure response is returned with the cookie

        return render_template("login.html", error="Invalid credentials!")
    
    return render_template("login.html")
