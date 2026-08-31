from flask import (
redirect,
render_template,
flash,
url_for,
Blueprint,
request,
session
)

from app.models import Students
from app import db

student_bp = Blueprint("students", __name__)

@student_bp.route("/", methods=["GET"])
def view_students():
    if "id" not in session:
        return redirect(url_for("auth.login"))

    students = Students.query.all()

    return render_template(
    "students.html",
    students=students
    )


@student_bp.route("/add_students", methods=["GET", "POST"])
def add_students():
    if "id" not in session:
        return redirect(url_for("auth.login"))


    if request.method == "POST":
        email = request.form.get("email")
        name = request.form.get("name")
        age = request.form.get("age")
        class_name = request.form.get("class_name")
        subject = request.form.get("subject")

        student_existing = Students.query.filter_by(
            email=email
        ).first()

        if student_existing:
            flash("Student Already Exists", "danger")
            return redirect(
                url_for("students.view_students")
            )

        new_student = Students(
            email=email,
            name=name,
            age=age,
            class_name=class_name,
            subject=subject
        )

        db.session.add(new_student)
        db.session.commit()

        flash("Student Added Successfully", "success")

        return redirect(
            url_for("students.view_students")
        )

    return render_template("add_students.html")
        
@student_bp.route("/delete/<int:students_id>", methods=["POST"])
def delete_students(students_id):

    if "id" not in session:
        return redirect(url_for("auth.login"))

    student = Students.query.get(students_id)

    if student:
        db.session.delete(student)
        db.session.commit()
        flash("Student Deleted Successfully", "success")

    return redirect(url_for("students.view_students"))