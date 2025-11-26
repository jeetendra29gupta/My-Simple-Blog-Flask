import markdown
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user

from src.config import bcrypt, login_manager
from src.forms import SignupForm, SigninForm, BlogForm
from src.models import User, db, Blog

main = Blueprint("main", __name__)


@main.route("/")
def index():
    page = request.args.get("page", 1, type=int)
    per_page = 3

    posts = (
        Blog.query.filter_by(status="published")
        .order_by(Blog.id.desc())
        .paginate(page=page, per_page=per_page)
    )
    return render_template("index.html", posts=posts)


@main.route("/read/<int:bid>")
def read_blog(bid):
    post = Blog.query.get_or_404(bid)
    post.body = markdown.markdown(post.body)
    return render_template("read-blog.html", post=post)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@main.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email_id=form.email_id.data).first()
        if existing_user:
            flash("Email already registered!", "Error")
            return redirect(url_for("main.signup"))

        hashed_password = bcrypt.generate_password_hash(form.password.data).decode(
            "utf-8"
        )

        user = User(
            fullname=form.fullname.data,
            email_id=form.email_id.data,
            password=hashed_password,
        )

        db.session.add(user)
        db.session.commit()

        flash("Account created successfully! Please sign in.", "Success")
        return redirect(url_for("main.signin"))

    return render_template("signup.html", form=form)


@main.route("/signin", methods=["GET", "POST"])
def signin():
    form = SigninForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email_id=form.email_id.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash(f"Welcome back, {user.fullname}!", "Success")
            next_page = request.args.get("next")
            return redirect(next_page or url_for("main.index"))

        flash("Invalid email or password!", "Error")
        return redirect(url_for("main.signin"))

    return render_template("signin.html", form=form)


@main.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "Success")
    return redirect(url_for("main.signin"))


@main.route("/blog/create", methods=["GET", "POST"])
@login_required
def create_blog():
    form = BlogForm()
    if form.validate_on_submit():
        new_blog = Blog(
            title=form.title.data,
            body=form.body.data,
            status=form.status.data,
            created_by=current_user.id,
        )
        db.session.add(new_blog)
        db.session.commit()
        flash("Blog post created successfully!", "Success")
        return redirect(url_for("main.blog"))

    return render_template("create-blog.html", form=form)


@main.route("/blog")
@login_required
def blog():
    page = request.args.get("page", 1, type=int)
    per_page = 3

    posts = (
        Blog.query.filter_by(created_by=current_user.id)
        .order_by(Blog.id.desc())
        .paginate(page=page, per_page=per_page)
    )
    return render_template("my-blog.html", posts=posts)


@main.route("/blog/status/<int:bid>")
@login_required
def toggle_status(bid):
    post = Blog.query.get_or_404(bid)
    if current_user.id != post.created_by:
        flash("Unauthorized action! You cannot access someone else's post.", "Error")
        return redirect(request.referrer or url_for("main.blog"))

    if post.status.value in ["draft", "unpublished"]:
        post.status = "published"
    else:
        post.status = "unpublished"

    db.session.commit()
    flash("Post status updated!", "Success")

    return redirect(request.referrer or url_for("main.blog"))


@main.route("/blog/view/<int:bid>")
@login_required
def view_blog(bid):
    post = Blog.query.get_or_404(bid)
    if current_user.id != post.created_by:
        flash("Unauthorized action! You cannot access someone else's post.", "Error")
        return redirect(request.referrer or url_for("main.blog"))
    post.body = markdown.markdown(post.body)
    return render_template("view-blog.html", post=post)


@main.route("/blog/delete/<int:bid>")
@login_required
def delete_blog(bid):
    post = Blog.query.get_or_404(bid)
    if current_user.id != post.created_by:
        flash("Unauthorized action! You cannot access someone else's post.", "Error")
        return redirect(request.referrer or url_for("main.blog"))

    db.session.delete(post)
    db.session.commit()
    flash("Post has been deleted successfully!", "Success")

    return redirect(url_for("main.blog"))


@main.route("/blog/edit/<int:bid>", methods=["GET", "POST"])
@login_required
def edit_blog(bid):
    post = Blog.query.get_or_404(bid)
    if current_user.id != post.created_by:
        flash("Unauthorized action! You cannot access someone else's post.", "Error")
        return redirect(request.referrer or url_for("main.blog"))

    form = BlogForm(obj=post)
    if form.validate_on_submit():
        post.title = form.title.data
        post.body = form.body.data
        post.status = form.status.data

        db.session.commit()

        flash("Blog updated successfully!", "Success")
        return redirect(url_for("main.blog"))

    return render_template("edit-blog.html", form=form, post=post)
