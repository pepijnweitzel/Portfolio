import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


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
    """Show portfolio of stocks"""
    # Get names of stocks owned by user
    list_of_stocks = db.execute("SELECT * FROM stocks WHERE users_id = ?", session["user_id"])

    # Get prices of stocks owned by user and input in list of dictionaries
    for i in range(len(list_of_stocks)):
        price = lookup(list_of_stocks[i]["stock"])["price"]
        list_of_stocks[i]["price"] = usd(price)
        amount_of_stocks = db.execute("SELECT number FROM stocks WHERE stock = ? AND users_id = ?", list_of_stocks[i]["stock"], session["user_id"])[0]["number"]
        list_of_stocks[i]["total_price"] = usd(int(price) * int(amount_of_stocks))
        list_of_stocks[i]["total_price_not_usd"] = int(price) * int(amount_of_stocks)

    # Get amount of cash
    cash_not_usd = int(db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]["cash"])
    cash = usd(cash_not_usd)

    # Add cash to the prices off all the stocks for TOTAL
    shares_total = 0
    for i in range(len(list_of_stocks)):
        shares_total += int(list_of_stocks[i]["total_price_not_usd"])
    shares_total = usd(shares_total + cash_not_usd)

    return render_template("index.html", list_of_stocks=list_of_stocks, cash=cash, total=shares_total)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    if request.method == "POST":
        # Ensure symbol was submitted
        if not request.form.get("symbol"):
            return apology("missing symbol", 400)
        # Ensure symbol exists in US marketplace
        elif not lookup(request.form.get("symbol")):
            return apology("inavlid symbol", 400)
        # Ensure shares was submitted and shares is positive number
        elif not request.form.get("shares") or int(request.form.get("shares")) < 1:
            return apology("missing shares", 400)
        else:
            info = lookup(request.form.get("symbol"))
            total_price = info["price"] * int(request.form.get("shares"))
            # Ensure user has enough cash
            userscash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]["cash"]
            if userscash < total_price:
                return apology("can't afford", 400)
            else:
                # Remove the total price from cash of user
                newcash = userscash - total_price
                db.execute("UPDATE users SET cash = ? WHERE id = ?", newcash, session["user_id"])
                # Add stock to user
                number_shares = request.form.get("shares")
                if len(db.execute("SELECT number FROM stocks WHERE users_id = ? AND stock = ?", session["user_id"], info["name"])) != 1:
                    db.execute("INSERT INTO stocks (users_id, stock, number) VALUES (?, ?, ?)", session["user_id"], info["name"], number_shares)
                else:
                    previous_amount = db.execute("SELECT number FROM stocks WHERE users_id = ? AND stock = ?", session["user_id"], info["name"])[0]["number"]
                    new_amount = int(previous_amount) + int(number_shares)
                    db.execute("UPDATE stocks SET number = ? WHERE users_id = ? AND stock = ?", new_amount, session["user_id"], info["name"])

        return redirect("/")
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    return apology("TODO")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    if request.method == "POST":
        # Ensure symbol was submitted
        if not request.form.get("symbol"):
            return apology("missing symbol", 400)
        # Ensure symbol exists in US marketplace
        elif not lookup(request.form.get("symbol")):
            return apology("inavlid symbol", 400)
        # Show the price of the given symbol stock
        else:
            info = lookup(request.form.get("symbol"))
            info["price"] = usd(info["price"])
            return render_template("quoted.html", symbol=info["name"], price=info["price"])
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)
        # Ensure username not already in use
        elif len(db.execute("SELECT username FROM users WHERE username = ?;", request.form.get("username"))) != 0:
            return apology("username already in use", 403)
        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)
        # Ensure confirmation was submitted
        elif not request.form.get("confirmation"):
            return apology("must provide repeated password", 403)
        # Ensure password matches confirmation
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("passwords do not match", 403)
        # Add user to userbase
        name = request.form.get("username")
        password = generate_password_hash(request.form.get("password"))
        db.execute("INSERT INTO users (username, hash) VALUES (?, ?);", name, password)
        # Sent to login page
        return login()
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    # Get names of all the owned stocks
    rows = db.execute("SELECT stock FROM stocks WHERE users_id = ?", session["user_id"])
    stock_names = []
    for row in rows:
        stock_names.append(row["stock"])

    # Check and try to sell given stock and the number of
    if request.method == "POST":
        # Ensure symbol was submitted
        if not request.form.get("symbol"):
            return apology("missing symbol", 400)
        # Ensure shares was submitted and it is a positive number
        elif not request.form.get("shares") or int(request.form.get("shares")) < 1:
            return apology("missing shares", 400)
        # Ensure user has enough shares to sell
        number_of_shares = db.execute("SELECT number FROM stocks WHERE useres_id = ? AND stock = ?", session["user_id"], request.form.get("symbol"))

        return redirect("/")
    else:
        return render_template("sell.html", stock_names=stock_names)
