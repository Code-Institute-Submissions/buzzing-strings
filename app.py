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


# Homepage
@app.route("/")
def about():
    """
    Renders the homepage
    """
    return render_template("pages/about.html")


# User Registration
@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Allows new user to register on the webpage,
    checks if the username already exists in database,
    puts the new user into 'session' cookie,
    redirects to user's profile if successfully registered
    """
    if request.method == "POST":
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

        session["user"] = request.form.get("username").lower()
        flash("Your registration was successful!")
        return redirect(url_for("guitars", username=session["user"]))
    return render_template("components/forms/register_form.html")


# User Login
@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Allows alredy registered user to log in,
    checks if the username already exists in database,
    ensures hashed password matches user input
    redirects to user's profile if successfully logged in
    """
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Hello, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "guitars", username=session["user"]))
            else:
                # invalid password match
                flash("Sorry, Your Username and/or Password is incorrect!")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Sorry, Your Username and/or Password is incorrect!")
            return redirect(url_for("login"))

    return render_template("components/forms/login_form.html")


# User Log Out
@app.route("/logout")
def logout():
    """
    Logs out the user,
    removes the user from session cookies
    """
    flash("Sorry, You have been log out!")
    session.pop("user")
    return redirect(url_for("about"))


@app.route("/user")
def user():
    return render_template("pages/user_list.html")


# 404 error page
@app.errorhandler(404)
def page_not_found(error):
    """
    Renders an error page with 404 message
    """
    error_message = str(error)
    return render_template("pages/error.html",
                           error_message=error_message), 404


@app.route("/guitars")
def guitars():
    guitars = mongo.db.guitars.find()
    return render_template("pages/guitars.html", guitars=guitars)


# 500 error page
@app.errorhandler(500)
def server_error(error):
    """
    Renders an error page with 500 message
    """
    error_message = str(error)
    return render_template("pages/error.html",
                           error_message=error_message), 500


if __name__ == '__main__':
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=os.environ.get("DEBUG"))