from flask import Flask
from flask_login import LoginManager
from models import db, User
from models.question import Question   
from routes import SamaYonne

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.secret_key = 'dokhol'

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

SamaYonne(app)

with app.app_context():
    db.create_all()

    if User.query.first() is None:
        tapha = User(id=1, username='tapha', password='123')
        talla = User(id=2,username='talla', password='123')
        db.session.add_all([tapha, talla])
        db.session.commit()


    if Question.query.first() is None:
        questions = [
            Question(
                id=1,
                question_text="Quel club a remporté le plus de titres en Premier League ?",
                choice_a="Chelsea",
                choice_b="Manchester United",
                choice_c="Liverpool",
                correct_answer='B'
            ),
            Question(
                id=2,
                question_text="Quel entraîneur a remporté le plus de titres avec Manchester City ?",
                choice_a="Pep Guardiola",
                choice_b="Roberto Mancini",
                choice_c="Manuel Pellegrini",
                correct_answer='A'
            ),
            Question(
                id=3,
                question_text="Qui est le meilleur buteur de l’histoire de la Premier League ?",
                choice_a="Thierry Henry",
                choice_b="Alan Shearer",
                choice_c="Wayne Rooney",
                correct_answer='B'
            ),
            Question(
                id=4,
                question_text="Quelle équipe est surnommée 'The Gunners' ?",
                choice_a="Tottenham",
                choice_b="Arsenal",
                choice_c="Manchester United",
                correct_answer='B'
            ),

            Question(
                id=5,
                question_text="Quel club a remporté le plus de titres de Liga ?",
                choice_a="Real Madrid",
                choice_b="FC Barcelone",
                choice_c="Atlético Madrid",
                correct_answer='A'
            ),
            Question(
                id=6,
                question_text="Quel joueur a marqué le plus de buts en Liga ?",
                choice_a="Cristiano Ronaldo",
                choice_b="Lionel Messi",
                choice_c="Karim Benzema",
                correct_answer='B'
            ),
            Question(
                id=7,
                question_text="Quel club est surnommé 'Los Colchoneros' ?",
                choice_a="Real Sociedad",
                choice_b="FC Barcelone",
                choice_c="Atlético Madrid",
                correct_answer='C'
            ),
            Question(
                id=8,
                question_text="En quelle année Cristiano Ronaldo a-t-il rejoint le Real Madrid ?",
                choice_a="2007",
                choice_b="2009",
                choice_c="2011",
                correct_answer='B'
            ),

            Question(
                id=9,
                question_text="Quel club a gagné le plus de titres en Serie A ?",
                choice_a="AC Milan",
                choice_b="Napoli",
                choice_c="Juventus",
                correct_answer='C'
            ),
            Question(
                id=10,
                question_text="Quel joueur est connu comme 'Il Fenomeno' ?",
                choice_a="Ronaldinho",
                choice_b="Ronaldo Nazário",
                choice_c="Zlatan Ibrahimović",
                correct_answer='B'
            ),
            Question(
                id=11,
                question_text="Quel club porte les couleurs noir et bleu en Serie A ?",
                choice_a="Inter Milan",
                choice_b="Napoli",
                choice_c="Lazio",
                correct_answer='A'
            ),
            Question(
                id=12,
                question_text="Quel joueur a été le capitaine emblématique de l'AS Roma ?",
                choice_a="Andrea Pirlo",
                choice_b="Francesco Totti",
                choice_c="Del Piero",
                correct_answer='B'
            ),

            Question(
                id=13,
                question_text="Quel club a dominé la Bundesliga ces dernières années ?",
                choice_a="Bayer Leverkusen",
                choice_b="Borussia Dortmund",
                choice_c="Bayern Munich",
                correct_answer='C'
            ),
            Question(
                id=14,
                question_text="Quel club est surnommé 'Die Borussen' ?",
                choice_a="Borussia Dortmund",
                choice_b="Bayern Munich",
                choice_c="RB Leipzig",
                correct_answer='A'
            ),
            Question(
                id=15,
                question_text="Qui est le meilleur buteur de l’histoire de la Bundesliga ?",
                choice_a="Gerd Müller",
                choice_b="Lewandowski",
                choice_c="Timo Werner",
                correct_answer='A'
            ),
            Question(
                id=16,
                question_text="Quel est le stade du Bayern Munich ?",
                choice_a="Signal Iduna Park",
                choice_b="Allianz Arena",
                choice_c="Olympiastadion",
                correct_answer='B'
            ),

            Question(
                id=17,
                question_text="Quel club a remporté la Ligue 1 en 2021 ?",
                choice_a="PSG",
                choice_b="Monaco",
                choice_c="Lille",
                correct_answer='C'
            ),
            Question(
                id=18,
                question_text="Quel club français a gagné la Ligue des Champions ?",
                choice_a="PSG",
                choice_b="Lyon",
                choice_c="Marseille",
                correct_answer='C'
            ),
            Question(
                id=19,
                question_text="Quel est le stade de l’Olympique de Marseille ?",
                choice_a="Stade Vélodrome",
                choice_b="Parc des Princes",
                choice_c="Groupama Stadium",
                correct_answer='A'
            ),
            Question(
                id=20,
                question_text="Qui est le meilleur buteur historique de l’OM ?",
                choice_a="Jean-Pierre Papin",
                choice_b="Didier Drogba",
                choice_c="Dimitri Payet",
                correct_answer='A'
            ),
        ]
        db.session.add_all(questions)
        db.session.commit()

    
