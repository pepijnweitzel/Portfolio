import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
import time

# Import functions from other file
from helpers import login_required, apology

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

@app.route("/logout")
def logout():

    # Forget the user_id (cookie)
    session.clear()

    # Redirect user to login page by sending to index page.
    return redirect("/")

@app.route("/profile")
def profile():



    if request.method == "POST":
        # If submitted execute this:
        if request.form.get("new_username"):
            new_name = request.form.get("new_username")
            old_name = db.execute("SELECT username FROM users WHERE id = ?;", session["user_id"])[0]["username"]
            # If new username is similar to old username changing it has no use
            if new_name == old_name:
                return apology("test", 400)
            else:
                # Update username to new username
                db.execute("UPDATE users SET username = ? WHERE id = ?;", new_name, session["user_id"])
        # If both passwords have been submitted check whether they are the same, and if not, update new password
        elif request.form.get("new_password"):
            new_password = request.form.get("new_password")
            if request.form.get("confirmation"):
                confirmation = request.form.get("confirmation")
                if new_password != confirmation:
                    return render_template("profile.html")
                else:
                    old_password_hashed = db.execute("SELECT hash FROM users WHERE id = ?;", session["user_id"])[0]["username"]
                    new_password_hashed = generate_password_hash(new_password)
                    # If passwords are the same:
                    if old_password_hashed == new_password_hashed:
                        return render_template("profile.html")
                    else:
                        # Update password
                        db.execute("UPDATE users SET hash = ? WHERE id = ?;", new_password_hashed, session["user_id"])
                        return redirect("/")

        return redirect("/")


    else:
        return render_template("profile.html", username=old_name)


