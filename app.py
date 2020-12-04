import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# About Us

@app.route("/")
@app.route("/about_us")
def about_us():
    return render_template("about_us.html")


# Guitars

@app.route("/guitars_list")
def guitars_list():
    guitars = mongo.db.guitars.find()
    return render_template("guitars.html", guitars=guitars)


# User register 

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if the username already exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Sorry, username already exists!")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put new user into a 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Well done, your registration was successful!")
    return render_template("register.html")


# User login

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if the user already exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}! Enjoy your visit!".format(request.form.get("username")))
            else:
                # invalid password match
                flash("Your Username or/and Password is incorrect!")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Your Username or/and Password is incorrect!")
            return redirect(url_for("login"))

    return render_template("login.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=os.environ.get("DEBUG"))