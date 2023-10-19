import os

from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from time import ctime
from datetime import datetime

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

@app.route("/", methods=["GET", "POST"])
@login_required
def index():

    # Declare variables
    users_groupcode = db.execute("SELECT groupcode FROM users WHERE id = ?;", session["user_id"])[0]["groupcode"]
    number_of_cars = len(db.execute("SELECT * FROM cars WHERE car_groupcode = ?;", users_groupcode))
    list_of_dicts_with_carnames = db.execute("SELECT car_name FROM cars WHERE car_groupcode = ?;", users_groupcode)
    car_names = []
    for i in range(len(list_of_dicts_with_carnames)):
        car_names.append(list_of_dicts_with_carnames[i]["car_name"])
    car_info_list = []
    for car_name in car_names:
        kilometercount = db.execute("SELECT kilometercount FROM cars WHERE car_name = ? AND car_groupcode = ?;", car_name, users_groupcode)[0]["kilometercount"]
        car_info_list.append([car_name, kilometercount])

    if request.method == "POST":

        # Check wheter they want to make reservation(left-side) or adjustment(right-side)
        if not request.form.get("car_name_reservation") and not request.form.get("starting_hour") and not request.form.get("ending_hour") and not request.form.get("reservations_day") and not request.form.get("starting_hour_removing") and not request.form.get("ending_hour_removing") and not request.form.get("car_name_removing") and not request.form.get("removing_day"):
            # Check whether they inputted any box
            if not request.form.get("car_name") and not request.form.get("kilometer_count"):
                if not request.form.get("new_car"):
                    if not request.form.get("remove_car"):
                        return apology("can't submit without any input", 400)
                    # Check for errors with removing car otherwise, remove it
                    elif request.form.get("remove_car") not in car_names:
                        return apology("car name incorrect", 400)
                    else:
                        db.execute("DELETE FROM cars WHERE car_name = ? AND car_groupcode = ?", request.form.get("remove_car"), users_groupcode)
                        return redirect("/")
                # Check for errors with adding new car otherwise (max 4 cars), add it
                elif request.form.get("new_car") in car_names:
                    return apology("car already exists", 400)
                elif len(db.execute("SELECT car_name FROM cars WHERE car_groupcode = ?;", users_groupcode)) > 3:
                    return apology("maximum number of cars is 4", 400)
                else:
                    db.execute("INSERT INTO cars (car_name, car_groupcode) VALUES (?, ?);", request.form.get("new_car"), users_groupcode)
                    return redirect("/")
            # Check whether they inputted both and not just 1:
            elif request.form.get("car_name") and not request.form.get("kilometer_count"):
                return apology("please give kilometer count", 400)
            elif not request.form.get("car_name") and request.form.get("kilometer_count"):
                return apology("please choose a car", 400)
            # Change kilometercount of car
            else:
                newkilometercount = request.form.get("kilometer_count")
                current_carname = request.form.get("car_name")
                db.execute("UPDATE cars SET kilometercount = ? WHERE car_groupcode = ? AND car_name = ?;", newkilometercount, users_groupcode, current_carname)
                # Add adjustment to adjustments table
                current_time = ctime()
                car_id = db.execute("SELECT id FROM cars WHERE car_name = ? AND car_groupcode = ?;", current_carname, users_groupcode)[0]["id"]
                usersname = db.execute("SELECT username FROM users WHERE id = ?;", session["user_id"])[0]["username"]

                db.execute("INSERT INTO adjustments (cars_id, new_kilometercount, datetime, usersname, car_name) VALUES (?, ?, ?, ?, ?)", car_id, newkilometercount, current_time, usersname, current_carname)
                return redirect("/")
        # If they  submitted reservation(left-side)
        # Check whether they want to remove a reservation or add one
        elif not request.form.get("car_name_reservation") and not request.form.get("starting_hour") and not request.form.get("ending_hour") and not request.form.get("reservations_day"):
            if not request.form.get("car_name_removing"):
                return apology("please give car name for removing", 400)
            elif not request.form.get("starting_hour_removing"):
                return apology("please give starting hour", 400)
            elif not request.form.get("ending_hour_removing"):
                return apology("please give ending hour", 400)
            elif not request.form.get("removing_day"):
                return apology("please give day of reservation", 400)
            elif len(db.execute("SELECT * FROM calendar WHERE cars_name = ? AND begin_time = ? AND end_time = ? and day = ?;", request.form.get("car_name_removing"), request.form.get("starting_hour_removing"), request.form.get("ending_hour_removing"), request.form.get("removing_day"))) == 0:
                return apology("No reservation with that data", 400)
            else:
                db.execute("DELETE FROM calendar WHERE cars_name = ? AND begin_time = ? AND end_time = ? and day = ?;", request.form.get("car_name_removing"), request.form.get("starting_hour_removing"), request.form.get("ending_hour_removing"), request.form.get("removing_day"))
                return redirect("/")
        else:
            # Check for errors:
            if not request.form.get("car_name_reservation"):
                return apology("please give car name for reservation", 400)
            elif not request.form.get("starting_hour"):
                return apology("please give starting hour", 400)
            elif not request.form.get("ending_hour"):
                return apology("please give ending hour", 400)
            elif int(request.form.get("starting_hour")) >= int(request.form.get("ending_hour")):
                return apology("please give a correct time frame")
            elif not request.form.get("reservations_day"):
                return apology("please give day of reservation", 400)
            # Check whether time frame not possible
            elif len(db.execute("SELECT * FROM calendar WHERE cars_name = ? AND day = ?;", request.form.get("car_name_reservation"), request.form.get("reservations_day"))) != 0:
                for row in db.execute("SELECT * FROM calendar WHERE cars_name = ? AND day = ?;", request.form.get("car_name_reservation"), request.form.get("reservations_day")):
                    existing_begin = row["begin_time"]
                    existing_end = row["end_time"]
                    using_hours = []
                    for i in range(existing_begin, existing_end):
                        using_hours.append(int(i))
                    asking_begin = int(request.form.get("starting_hour"))
                    asking_end = int(request.form.get("ending_hour"))
                    if asking_begin in using_hours or asking_end in using_hours:
                        return apology("time-frame not possible", 400)
                # Declare variables
                car_name_reservation = request.form.get("car_name_reservation")
                usersname = db.execute("SELECT username FROM users WHERE id = ?;", session["user_id"])[0]["username"]
                begin_time = int(request.form.get("starting_hour"))
                end_time = int(request.form.get("ending_hour"))
                reservations_day = int(request.form.get("reservations_day"))
                # Input data into database
                db.execute("INSERT INTO calendar (cars_name, usersname, begin_time, end_time, day) VALUES (?, ?, ?, ?, ?);", car_name_reservation, usersname, begin_time, end_time, reservations_day)
                return redirect("/")
            # If no errors execute following
            else:
                # Declare variables
                car_name_reservation = request.form.get("car_name_reservation")
                usersname = db.execute("SELECT username FROM users WHERE id = ?;", session["user_id"])[0]["username"]
                begin_time = int(request.form.get("starting_hour"))
                end_time = int(request.form.get("ending_hour"))
                reservations_day = int(request.form.get("reservations_day"))
                # Input data into database
                db.execute("INSERT INTO calendar (cars_name, usersname, begin_time, end_time, day) VALUES (?, ?, ?, ?, ?);", car_name_reservation, usersname, begin_time, end_time, reservations_day)
                return redirect("/")

    # Give page if GET method
    else:
        if session["user_id"]:
            # Get rid of old reservations
            date_right_now = datetime.now().day
            day_1 = date_right_now - 1
            day_2 = date_right_now - 2
            day_3 = date_right_now - 3
            db.execute("DELETE FROM calendar WHERE day = ? or day = ? or day = ?;", day_1, day_2, day_3)
            # Create table to show car reservations
            # Declare variables
            usersname = db.execute("SELECT username FROM users WHERE id = ?;", session["user_id"])[0]["username"]
            if number_of_cars == 0:
                rows = db.execute("SELECT * FROM calendar WHERE usersname = ?;", usersname)
                
            elif number_of_cars == 1:
                rows = db.execute("SELECT * FROM calendar WHERE cars_name = ? AND usersname = ?;", car_names[0], usersname)

            elif number_of_cars == 2:
                rows = db.execute("SELECT * FROM calendar WHERE cars_name = ? OR cars_name = ? AND usersname = ?;", car_names[0], car_names[1], usersname)

            elif number_of_cars == 3:
                rows = db.execute("SELECT * FROM calendar WHERE cars_name = ? OR cars_name = ? OR cars_name = ? AND usersname = ?;", car_names[0], car_names[1], car_names[2], usersname)

            else:
                rows = db.execute("SELECT * FROM calendar WHERE cars_name = ? OR cars_name = ? OR cars_name = ? OR cars_name = ? AND usersname = ?;", car_names[0], car_names[1], car_names[2], car_names[3], usersname)

            return render_template("index.html", number_of_cars=number_of_cars, car_names=car_names, car_info_list=car_info_list, rows=rows)
        else:
            return render_template("index.html", number_of_cars=number_of_cars, car_names=car_names, car_info_list=car_info_list)

@app.route("/login", methods=["GET", "POST"])
def login():

    # Forget any user_id
    session.clear()

    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("please give username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("please give password", 400)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("username or password is wrong", 400)

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
            return apology("please give username", 400)
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
            return apology("username already in use", 400)
        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("please give password", 400)
        # Ensure confirmation was submitted
        elif not request.form.get("confirmation"):
            return apology("please give repeated password", 400)
        # Ensure password matches confirmation
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("passwords do not match", 400)
        # Check whether they inputted nothing at group codes
        elif not request.form.get("group_code_join") and not request.form.get("group_code_create"):
            return apology("please give a group code or create one", 400)
        # Check whether they inputted something in both group codes
        elif request.form.get("group_code_join") and request.form.get("group_code_create"):
            return apology("please only give one group code", 400)
        # Check whether they inputted create or join with group code
        elif request.form.get("group_code_join"):
            if (len(db.execute("SELECT groupcode FROM users WHERE groupcode = ?;", request.form.get("group_code_join")))) == 0:
                return apology("groupcode does not exist", 400)
            else:
                #if the code is found in database, it exists and they can join the group
                db.execute(
                    "INSERT INTO users (username, hash, groupcode) VALUES (?, ?, ?);",
                    request.form.get("username"), generate_password_hash(request.form.get("password")), request.form.get("group_code_join")
                )

                # Redirect user to home page
                return login()
        else:
            if len(
                db.execute(
                    "SELECT groupcode FROM users WHERE groupcode = ?;",
                    request.form.get("group_code_create")
                )
            ) != 0:
                #if the code is found in the database, it already exists and they need to come up with another one
                return apology("code already in use", 400)
            else:
                db.execute(
                    "INSERT INTO users (username, hash, groupcode) VALUES (?, ?, ?);",
                    request.form.get("username"), generate_password_hash(request.form.get("password")), request.form.get("group_code_create")
                )

                # Redirect user to home page
                return login()

    # If get:
    else:
        return render_template("register.html")

@app.route("/logout")
def logout():

    # Forget the user_id (cookie)
    session.clear()

    # Redirect user to login page by sending to index page.
    return redirect("/")

@app.route("/profile", methods=["GET", "POST"])
@login_required
def profile():



    if request.method == "POST":
        # If submitted execute this:
        if request.form.get("new_username"):
            new_name = request.form.get("new_username")
            old_name = db.execute("SELECT username FROM users WHERE id = ?;", session["user_id"])[0]["username"]
            # If new username is similar to old username changing it has no use
            if new_name == old_name:
                return apology("you already have that username", 400)
            elif len(db.execute("SELECT username FROM users WHERE username = ?;", new_name)) != 0:
                return apology("username already in use", 400)
            else:
                # Update username to new username
                db.execute("UPDATE users SET username = ? WHERE id = ?;", new_name, session["user_id"])
        # If both passwords have been submitted check whether they are the same, and if so, update new password
        elif request.form.get("new_password"):
            new_password = request.form.get("new_password")
            if request.form.get("confirmation"):
                confirmation = request.form.get("confirmation")
                if new_password != confirmation:
                    return apology("passwords do not match", 400)
                else:
                    new_password_hashed = generate_password_hash(new_password)
                    # Update password
                    db.execute("UPDATE users SET hash = ? WHERE id = ?;", new_password_hashed, session["user_id"])
                    return redirect("/")

        return redirect("/")


    else:
        username = db.execute("SELECT username FROM users WHERE id = ?;", session["user_id"])[0]["username"]
        return render_template("profile.html", username=username)

@app.route("/history")
@login_required
def history():

    # Get variables to call for correct history table
    car_ids = []
    current_groupcode = db.execute("SELECT groupcode FROM users WHERE id = ?;", session["user_id"])[0]["groupcode"]
    list_of = db.execute("SELECT id FROM cars WHERE car_groupcode = ?;", current_groupcode)
    for i in range(len(list_of)):
        car_ids.append(list_of[i]["id"])
    # Make all ids an integer
    for id in car_ids:
        id = int(id)
        db.execute("INSERT INTO temporary (temp_ids) VALUES (?);", id)
    # now do a db.execute with all those id's for the history of it.
    rows = db.execute("SELECT new_kilometercount, datetime, usersname, car_name FROM adjustments WHERE cars_id IN ?;", "temporary")

    for id in car_ids:
        db.execute("DELETE FROM temporary WHERE temp_ids = ?;", id)

    return render_template("history.html", rows=rows)