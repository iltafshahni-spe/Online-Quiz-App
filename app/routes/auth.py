
from flask import (
    render_template,
    url_for,
    session,
    redirect,
    flash,
    request,
    Blueprint
)

from app import db
from app.models import User, Students
from werkzeug.security import generate_password_hash, check_password_hash

auth_pb = Blueprint("auth", __name__)


@auth_pb.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email")
        name = request.form.get("name")
        password = request.form.get("password")

        user_exists = User.query.filter_by(email=email).first()

        if user_exists:
            flash("User Already Exists", "danger")
            return redirect(url_for("auth.register"))

        hashed_password = generate_password_hash(password)

        new_user = User(
            email=email,
            name=name,
            password=hashed_password
        )

        db.session.add(new_user)
        db.session.commit()

        flash("Registered Successfully", "success")
        return redirect(url_for("auth.login"))

    return render_template("register.html")


@auth_pb.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        name = request.form.get("name")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            session["id"] = user.id
            session["email"] = user.email

            flash("Login Successful", "success")

            return redirect(url_for("auth.dashboard"))

        flash("Invalid Email or Password", "danger")

    return render_template("login.html")


@auth_pb.route("/students")
def dashboard():
    if "id" not in session:
        return redirect(url_for("auth.login"))

    students = Students.query.all()

    return render_template(
        "students.html",
        students=students
    )


@auth_pb.route("/add_students", methods=["GET", "POST"])
def add_students():
    if "id" not in session:
        return redirect(url_for("auth.login"))

    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        class_name = request.form.get("class_name")
        email = request.form.get("email")
        subject = request.form.get("subject")

        new_student = Students(
            name=name,
            age=age,
            class_name=class_name,
            email=email,
            subject=subject
        )

        db.session.add(new_student)
        db.session.commit()

        flash("Student Added Successfully", "success")

        return redirect(url_for("auth.dashboard"))

    return render_template("add_students.html")


@auth_pb.route("/logout")
def logout():
    session.pop("id", None)
    session.pop("username", None)

    flash("Logged out successfully", "info")

    return redirect(url_for("auth.login"))

