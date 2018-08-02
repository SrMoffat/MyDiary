#views.py
from flask import request, render_template

from app import app

@app.route("/")
def index():
    """
    Render the index page
    """
    return render_template("index.html")

@app.route("/about")
def about():
    """
    Render the about us page
    """
    return render_template("about.html")

@app.route("/signup")
def signup():
    """
    Render the signup page
    """
    return render_template("signup.html")

@app.route("/login")
def login():
    """
    Render the login page
    """
    return render_template("signin.html")

@app.route("/dashboard")
def dashboard():
    """
    Render the dashboard page
    """
    return render_template("dashboard.html")

@app.route("/add")
def add_entry():
    """
    Render the index page
    """
    return render_template("addentry.html")

@app.route("/view")
def view_entry():
    """
    Render the view_entry page
    """
    return render_template("viewentry.html")

@app.route("/notifications")
def notifications():
    """
    Render the notifications page
    """
    return render_template("notifications.html")

@app.route("/profile")
def profile():
    """
    Render the user profile page
    """
    return render_template("profile.html")