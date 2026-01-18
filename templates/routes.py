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

@app.route("/post/new", methods = [GET, POST])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit:
        post = Post(title = form.title.data, content = form.content.data, author = current_user)
        db.session.add(post)
        db.session.commit()
        flash("Your task has been created!", "success")
        return redirect(url_for('home'))
    return render_template('create_post.html', title = 'New Task', form = form, legend = "New Task")


@app.route("/post/int:post_id")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title = post.title, post = post)

@app.route("/post/<int:post_id>/update", methods= [GET, POST])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.content.data
        db.session.commit()
        flash("Your task has been updated!", "success")
        return redirect(url_for("post", post_id = post_id))
    elif request.method == "GET":
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title = "Update Task", form = form, legend = "Update Task")

@app.route("/post/<int:post_id>/delete", methods = ["POST"])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash("Your task has been deleted!", 'success')
    return redirect(url_for("home"))
