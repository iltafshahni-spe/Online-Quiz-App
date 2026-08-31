from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():

    app = Flask(__name__)

    app.config["SECRET_KEY"] = "secret-key"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///quiz.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    from app.models import User, Students, Question
    from app.routes.auth import auth_pb
    from app.routes.students import student_bp
    from app.routes.question import question_bp
    from app.routes.quiz import quiz_bp


    app.register_blueprint(auth_pb)
    app.register_blueprint(student_bp)
    app.register_blueprint(question_bp)
    app.register_blueprint(quiz_bp)

    return app