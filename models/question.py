from . import db

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String(255), nullable=False)
    choice_a = db.Column(db.String(100), nullable=False)
    choice_b = db.Column(db.String(100), nullable=False)
    choice_c = db.Column(db.String(100), nullable=False)
    correct_answer = db.Column(db.String(1), nullable=False)
