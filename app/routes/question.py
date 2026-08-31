from flask import (
    session,
    flash,
    render_template,
    request,
    redirect,
    url_for,
    Blueprint
)

from app import db
from app.models import Question

question_bp = Blueprint("question", __name__)


@question_bp.route("/add_question", methods=["GET", "POST"])
def add_question():

    if "id" not in session:
        return redirect(url_for("auth.login"))

    if request.method == "POST":

        question = request.form.get("question")
        option_a = request.form.get("option_a")
        option_b = request.form.get("option_b")
        option_c = request.form.get("option_c")
        option_d = request.form.get("option_d")
        correct_answer = request.form.get("correct_answer")

        new_question = Question(
            question=question,
            option_a=option_a,
            option_b=option_b,
            option_c=option_c,
            option_d=option_d,
            correct_answer=correct_answer
        )

        db.session.add(new_question)
        db.session.commit()

        flash("Question Added Successfully", "success")

        return redirect(url_for("question.view_question"))

    return render_template("question_add.html")


@question_bp.route("/quiz")
def view_question():

    if "id" not in session:
        return redirect(url_for("auth.login"))

    questions = Question.query.all()

    return render_template(
        "quiz.html",
        questions=questions
    )