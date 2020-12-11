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
@app.route('/')
def about():
    """
    The function lrenders the homepage
    """
    return render_template('pages/about.html')


@app.route('/register', methods=["GET", "POST"])
def register():
    """
    Allows new user to register on the webpage,
    checks if the username already exists in database
    """
    


@app.route('/login', methods=["GET", "POST"])
def login():
    """
    Allows alredy registered user to log in
    """

# Guitars
@app.route('/guitars')
def guitars():
    """
    It loads the guitars page
    Allows the user to check a list of guitars
    """
    guitars = mongo.db.guitars.find()
    return render_template('pages/guitars.html', guitars=guitars)


# 404 error page
@app.errorhandler(404)
def page_not_found():
    """
    Renders an error page with 404 message
    """
    error_message = str(error)
    return render_template('pages/error.html',
                           error_message=error_message), 400


# 500 error page
@app.errorhandler(500)
def server_error():
    """
    Renders an error page with 500 message
    """
    error_message = str(error)
    return render_template('pages/error.html',
                           error_message=error_message), 500


if __name__ == '__main__':
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=os.environ.get("DEBUG"))