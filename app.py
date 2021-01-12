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
        return redirect(url_for("all_guitars", username=session["user"]))
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
                       "all_guitars", username=session["user"]))
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


# All Guitars
@app.route("/all_guitars")
def all_guitars():
    """
    Renders all guitars page
    """
    guitars = list(mongo.db.guitars.find())
    return render_template("pages/all_guitars.html", guitars=guitars)


# Add Guitar
@app.route("/add_guitar", methods=["GET", "POST"])
def add_guitar():
    """
    Enables the user to choose the guitar type,
    allows the user to add a new guitar
    """
    if request.method == "POST":
        guitar = {
            "guitar_type": request.form.get("guitar_type"),
            "guitar_name": request.form.get("guitar_name"),
            "guitar_shape": request.form.get("guitar_shape"),
            "guitar_description": request.form.get("guitar_description"),
            "guitar_image": request.form.get("guitar_image"),
            "date_added": request.form.get("date_added"),
            "added_by": request.form.get("added_by")
        }
        mongo.db.guitars.insert_one(guitar)
        flash("Well done, Your Guitar was successfully added!")
        return redirect(url_for("all_guitars"))
    guitar_categories = mongo.db.guitar_categories.find().sort(
            "guitar_type", 1)
    return render_template(
            "components/forms/add_guitar.html",
            guitar_categories=guitar_categories)


# Edit guitar
@app.route("/edit_guitar/<guitar_id>", methods=["GET", "POST"])
def edit_guitar(guitar_id):
    """
    Allows to edit guitar content added by the user,
    enables the user to submit the changes,
    allows the user to cancel the updated changes
    """
    if request.method == "POST":
        submit = {
            "guitar_type": request.form.get("guitar_type"),
            "guitar_name": request.form.get("guitar_name"),
            "guitar_shape": request.form.get("guitar_shape"),
            "guitar_description": request.form.get("guitar_description"),
            "guitar_image": request.form.get("guitar_image"),
            "date_added": request.form.get("date_added"),
            "added_by": request.form.get("added_by")
        }
        mongo.db.guitars.update({"_id": ObjectId(guitar_id)}, submit)
        flash("Well done, your guitar was successfully updated!")
        return redirect(url_for("all_guitars"))

    guitar = mongo.db.guitars.find_one({"_id": ObjectId(guitar_id)})
    guitar_categories = mongo.db.guitar_categories.find().sort(
            "guitar_type", 1)
    return render_template(
            "pages/edit_guitar.html", guitar=guitar,
            guitar_categories=guitar_categories)


# Delete guitar
@app.route("/delete_guitar/<guitar_id>")
def delete_guitar(guitar_id):
    """
    Allows the user to delete guitar content
    """
    mongo.db.guitars.remove({"_id": ObjectId(guitar_id)})
    flash("Your Guitar was successfully deleted!")
    return redirect(url_for("all_guitars"))


# 404 error page
@app.errorhandler(404)
def page_not_found(error):
    """
    Renders an error page with 404 message
    """
    error_message = str(error)
    return render_template("pages/error.html",
                           error_message=error_message), 404


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