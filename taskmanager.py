from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect 
from flask_sqlalchemy import SQLAlchemy
app = Flask(_name_)
app.config('SECRET KEY') = 
app.config('SQLALCHEMY_DATABBASE_URI') = ''
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    password = db.Column(db.String(60), nullable = False)
    tasks = db.relationship("Task", backref = "Author", lazy = True)

    
#Need to have in progress for a task as a status, and need to have completed as a status

class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    date_posted = db.Column(db.DateTIme, nullabe = False, default = datetime.utcnow)
    content = db.Column(db.Text, nullable = False)
    user_id = db.COlumn(db.Integer, db.ForiegnKey('user.id'),nullable = False)


@app.route("/create")
def create():

app.route("/delete")
def delete():
