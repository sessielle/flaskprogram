"""Flask program with several sites that allow users to navigate through"""
from datetime import datetime
from flask import Flask, render_template, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from __init__ import db
from models import User

app = Flask(__name__)

db = SQLAlchemy()
app.config["SECRET_KEY"] = "thisisthesecret"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://db.sqlite3"


@app.route('/', methods =["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == "test" and form.password.data == "tester":
            return redirect(url_for("home"))
        elif form.username.data != "test" and form.password.data != "tester":
            return redirect(url_for("signup"))
    return render_template("login.html", form=form)


@app.route('/signup', methods=["POST", "GET"])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,email=form.email.data,password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("signup.html", form=form)


@app.route('/home', methods=["GET", "POST"])
def home():
    """Home page for all general information"""
    # show date and time
    date = datetime.now()
    return render_template("home.html") + date.strftime("\n %h %d, %Y  -  %H:%M:%S")


@app.route('/about')
def about_movies():
    """About page for detailed who, what, why"""
    date = datetime.now()
    return render_template("about.html") + date.strftime("\n %h %d, %Y  -  %H:%M:%S")


@app.route('/movie')
def movie_page():
    """List of movies on page"""
    date = datetime.now()
    return render_template("movie.html") + date.strftime("\n %h %d, %Y  -  %H:%M:%S")


@app.route('/wildlife')
def wild_life():
    """Wildlife documentary page showcase notable wildlife docus"""
    date = datetime.now()
    return render_template("wildlife.html") + date.strftime("\n %h %d, %Y  -  %H:%M:%S")


@app.route('/wildcard')
def wild_card():
    """Documentary page to list out other notable wildcard docus"""
    date = datetime.now()
    return render_template("wildcard.html") + date.strftime("\n %h %d, %Y  -  %H:%M:%S")


if __name__ == '__main__':
    app.run()
