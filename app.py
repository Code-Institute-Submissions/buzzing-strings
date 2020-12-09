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


# About
@app.route('/')
def about():
    """
    The function loads the about page
    """
    return render_template('pages/about.html')


# Register
@app.route('/register', methods=["GET", "POST"])
def register():
    """
    Allows new user to registe on the webpage
    It checks if the username already exists in database
    Redirects the user to guitars page
    """
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Sorry, this username already exists!")
            return redirect(url_for("register"))

        username = request.form.get("username").lower()
        password = generate_password_hash(request.form.get("pasword"))

        mongo.db.users.insert_one({
            'username': username,
            'password': password})
 
        if mongo.db.users.find_one({'username': username}) is not None:
            user = mongo.db.users.find_one({'username': username})
            user_id = user['_id']
            session['user_id'] = str(user_id)
            guitars = mongo.db.guitars({"user_id": user_id})
            return redirect(user_id=user_id)

    return render_template(url_for(
            'pages/user_authentication.html', register=True))


# Guitars
@app.route('/guitars')
def guitars():
    """
    It loads the guitars page
    Allows the user to check a list of guitars
    """
    guitars = mongo.db.guitars.find()
    return render_template('pages/guitars.html', guitars=guitars)


if __name__ == '__main__':
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=os.environ.get("DEBUG"))