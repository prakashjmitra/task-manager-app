from flask import render_template, url_for, flash, redirect
from taskmanager import app
from taskmanager.models import User, Task
from taskmanager.forms import RegistrationForm, LoginForm

tasks = [
    {
        "author" : "Prakash Mitra",
        "title" : "Task 1",
        "content" : "Task content",
        "date_posted" : "January 15, 2026"
    },
    {
        "author" : "John Doe",
        "title" : "Task 2",
        "content" : "Task 2 content",
        "date_posted" : "January 16, 2026"
    }

]
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts = tasks)

@app.route("/about")
def about():
    return render_template("about.html", title = "About")
@app.route("/register", methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!","success")
        return redirect(url_for("home"))
    return render_template("register.html", title = "Register", form = form)

@app.route("/login", methods = ["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password == "password:
            flash("You have been logged in!", "success")
            return redirect(url_for("home"))
        else:
            flash("Login Unsuccessful, please check username or password", "danger")
    return render_template("login.html", title = "Login", form = form)