from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from datetime import datetime

import sqlite3
app = Flask(__name__)
app.secret_key = 'team30'  # Change this to a secure secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    mobile = db.Column(db.String(15), unique=True, nullable=False)
    study_class = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(60), nullable=False)

# Define subjects for each day
schedule = {
    "Monday": ["CDSS", "LIBRARY", "TEA BREAK", "CDSS LAB FOR D1 && CN LAB FOR D2", "LUNCH BREAK", "PROFESSIONAL-ELECTIVE 3"],
    "Tuesday": ["CC", "CDSS", "TEA BREAK", "OPEN ELECTIVE 2","OPEN ELECTIVE 2", "LUNCH BREAK", "PROFESSIONAL-ELECTIVE 2", "CN"],
    "Wednesday": ["CDSS LAB FOR D2 && CN LAB FOR D1", "TEA BREAK", "CC", "LIBRARY", "LUNCH BREAK", "PROFESSIONAL-ELECTIVE 3"],
    "Thursday": ["LIBRARY", "CN", "TEA BREAK", "LIBRARY", "CDSS", "LUNCH BREAK", "PROFESSIONAL-ELECTIVE 2", "OPEN ELECTIVE 2"],
    "Friday": ["CN", "CDSS", "TEA BREAK", "LIBRARY", "CC"],
    "Saturday": [],
    "Sunday": []  # No schedule on Sunday
}



@app.route('/')
def home():
    return render_template('login.html')

@app.route('/subjects')
def subjects():
    return render_template('subjects.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        mobile = request.form['mobile']
        study_class = request.form['study_class']
        password = request.form['password']
        
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User(username=username, email=email, mobile=mobile, study_class=study_class, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            flash('Login successful', 'success')
            return redirect(url_for('subjects'))
        else:
            flash('Login failed. Check your email and password.', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    flash('Logged out successfully', 'info')
    return redirect(url_for('login'))

@app.route('/craft')
def craft():
    return render_template('craft.html')
@app.route('/mynotes')
def mynotes():
    return render_template('mynotes.html')

@app.route('/chatbot.html')
def chatbot():
    return render_template('chatbot.html')
 
@app.route('/quiz.html')
def quiz():
    return render_template('quiz.html')  
@app.route('/game.html')
def game():
    return render_template('game.html')
@app.route('/video')
def video():
    return render_template('index.html')
@app.route('/links')
def links():
    return render_template('links.html')
@app.route('/work_remainder')
def work_remainder():
    current_time = datetime.now()
    weekday = current_time.strftime("%A")  # Get the current weekday as a string

    weekday = datetime.today().strftime('%A')
    print("Today's weekday:", weekday)  # Print the weekday for debugging
    
    # Get schedule for today
    todays_schedule = schedule.get(weekday, [])
    print("Today's schedule:", todays_schedule)  # Print the schedule for debugging

    return render_template('work_remainder.html', schedule=todays_schedule, weekday=weekday)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True,port=8000)
