import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
import time

# Import functions from other file
from helpers import login_required

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///carshare.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
@login_required
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    # Forget any user_id
    session.clear()

    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return render_template("login.html")

        # Ensure password was submitted
        elif not request.form.get("password"):
            return render_template("login.html")

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return render_template("login.html")

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    else:
        return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():

    # If post:
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return render_template("register.html")
        # Ensure username not already in use
        elif (
            len(
                db.execute(
                    "SELECT username FROM users WHERE username = ?;",
                    request.form.get("username"),
                )
            )
            != 0
        ):
            return render_template("register.html")
        # Ensure password was submitted
        elif not request.form.get("password"):
            return render_template("register.html")
        # Ensure confirmation was submitted
        elif not request.form.get("confirmation"):
            return render_template("register.html")
        # Ensure password matches confirmation
        elif request.form.get("password") != request.form.get("confirmation"):
            return render_template("register.html")
        # Check whether they inputted nothing at group codes
        elif not request.form.get("group_code_join") and not request.form.get("group_code_create"):
            return render_template("register.html")
        # Check whether they inputted something in both group codes
        elif request.form.get("group_code_join") and request.form.get("group_code_create"):
            return render_template("register.html")
        # Check whether they inputted create or join with group code
        elif request.form.get("group_code_join"):
            if (len(db.execute("SELECT groupcode FROM users WHERE groupcode = ?;", request.form.get("group_code_join")))) == 0:
                return render_template("register.html")
            else:
                #if the code is found in database, it exists and they can join the group
                db.execute(
                    "INSERT INTO users (username, hash, groupcode) VALUES (?, ?, ?);",
                    request.form.get("username"), generate_password_hash(request.form.get("password")), request.form.get("group_code_join")
                )
                
                # Redirect user to home page
                login()
        else:
            if len(
                db.execute(
                    "SELECT groupcode FROM users WHERE groupcode = ?;",
                    request.form.get("group_code_create")
                )
            ) != 0:
                #if the code is found in the database, it already exists and they need to come up with another one
                return render_template("register.html")
            else:
                db.execute(
                    "INSERT INTO users (username, hash, groupcode) VALUES (?, ?, ?);",
                    request.form.get("username"), generate_password_hash(request.form.get("password")), request.form.get("group_code_create")
                )

                # Redirect user to home page
                login()

    # If get:
    else:
        return render_template("register.html")
