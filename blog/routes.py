# What the web requests will cause our website to do
from flask import Flask, render_template, url_for, flash, redirect, flash, request
from sqlalchemy import asc, desc
from blog import app, db
from blog.models import User, Post, Comment, Rating
from blog.forms import RatingForm, RegistrationForm, LoginForm, AddCommentForm, SortingForm
from flask_login import login_user, logout_user, current_user, login_required


@app.route("/")
@app.route("/home", methods=["GET", "POST"])
def home():
    posts = Post.query.all()
    form = SortingForm()
    if form.validate_on_submit():
        if form.sort_post.data == "date_asc": #sorting
            abc = Post.query.order_by(Post.date.asc()).all()
        else:
            abc = Post.query.order_by(Post.date.desc()).all()
        print(abc)
        return render_template("home.html", posts=abc, form=form)
    return render_template("home.html", posts=posts, form=form)


# Can also tell the server to look for other pages I want to add by adding routing information
@app.route("/about")
def about():
    return render_template("about.html", title="About Me")

@app.route("/privacy")
def privacy():
    return render_template("privacy.html", title="Privacy Policy")

@app.route("/contactdetails")
def contactdetails():
    return render_template("contactdetails.html", title="Contact Details")

@app.route("/disclaimer")
def disclaimer():
    return render_template("disclaimer.html", title="Disclaimer")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            password=form.password.data,
            email=form.email.data,
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)
        flash("Registration successful! Thank you!")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)


@app.route("/registered")
def registered():
    form = RegistrationForm()
    return render_template("registered.html", title="Thanks!")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            user
            login_user(user)
            flash("You've successfully logged in," + " " + current_user.username + "!")
            return redirect(url_for("home"))
        flash("Invalid username or password.")
    return render_template("login.html", title="Login", form=form)


@app.route("/logout")
def logout():
    logout_user()
    flash("You're now logged out. Thanks for your visit!")
    return redirect(url_for("home"))


@app.route("/post/<int:post_id>", methods=["GET", "POST"])
def post(post_id):
    post = Post.query.get_or_404(post_id)
    form = AddCommentForm()
    rating_form = RatingForm()
    ratings = Rating.query.filter_by(post_id = post.id).all()
    if (request.method == "POST"):  # this only gets executed when the form is submitted and not when the page loads
        if form.validate_on_submit(): #for comments
            comment = Comment(
                content=form.comment.data, post_id=post.id, author_id=current_user.id)
            comment.author_name = current_user.username
            db.session.add(comment)
            db.session.commit()
            flash("Your comment has been added to the post", "success")
            return redirect(f"/post/{post.id}")
        if rating_form.validate_on_submit(): #for ratings
            rating = Rating(rating_of_post=rating_form.rating.data,post_id=post.id, user_id=current_user.id)
            db.session.add(rating)
            db.session.commit()
            flash("Your rating has been added to the post", "success") 
            return redirect(f"/post/{post.id}")
    comment = Comment.query.filter(Comment.post_id == post.id)
    rating_sum = 0
    for rating in ratings:
        rating_sum= rating.rating_of_post + rating_sum
    average_rating = rating_sum/len(ratings)
    return render_template(
        "post.html", title="Comment Post", form=form, post_id=post_id, 
        post=post, comments=comment, average_rating=round(average_rating, 1), rating_form=rating_form
        )
