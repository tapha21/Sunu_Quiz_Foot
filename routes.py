# routes.py
from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from models.user import User
from models.question import Question
from models import db

def SamaYonne(app):

    @app.route('/')
    def home():
        return render_template('home.html')
    
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            user = User.query.filter_by(username=username, password=password).first()
            if user:
                login_user(user)
                return redirect(url_for('quiz'))
        return render_template('login.html')

    @app.route('/quiz', methods=['GET', 'POST'])
    def quiz():
        questions = Question.query.all() 
        if request.method == 'POST':
            score = 0
            for q in questions:
                if request.form.get(str(q.id)) == q.correct_answer:
                    score += 1
            current_user.score = score
            db.session.commit()
            return redirect(url_for('result'))
        return render_template('quiz.html', questions=questions)

    @app.route('/result')
    def result():
        return render_template('result.html', score=current_user.score)

    @app.route('/logout')
    def logout():
        logout_user()
        return redirect(url_for('login'))
