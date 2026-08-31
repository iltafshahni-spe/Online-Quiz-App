from flask import (
    Blueprint,
    render_template,
    request
)

from app.models import Question

quiz_bp = Blueprint("quiz", __name__)


@quiz_bp.route("/quiz", methods=["GET", "POST"])
def quiz():

    questions = Question.query.all()

    if request.method == "POST":

        score = 0

        for question in questions:

            answer = request.form.get(
                f"question_{question.id}"
            )

            if answer == question.correct_answer:
                score += 1

        return render_template(
            "result.html",
            score=score,
            total=len(questions)
        )

    return render_template(
        "quiz.html",
        questions=questions
    )