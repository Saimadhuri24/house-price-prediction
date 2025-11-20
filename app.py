from flask import Flask, render_template, request, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import pickle
import numpy as np
import pandas as pd
import os

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

# Create Database if not exists
with app.app_context():
    db.create_all()

# Load ML Model
model = pickle.load(open("model/best_model.pkl", "rb"))
encoder = model.named_steps['preprocessor'].named_transformers_['onehot']
locations = encoder.get_feature_names_out(['location'])
locations = sorted([loc.split('_')[-1] for loc in locations])


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        hashed_pw = generate_password_hash(password)

        user = User(username=username, password=hashed_pw)
        db.session.add(user)
        try:
            db.session.commit()
        except:
            return render_template("signup.html", msg="Username already exists!")
        return redirect(url_for('login'))

    return render_template("signup.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            session['user'] = username
            return redirect(url_for('predict_page'))
        else:
            return render_template("login.html", msg="Invalid Credentials!")

    return render_template("login.html")


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))


@app.route('/predict_page')
def predict_page():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template("index.html", locations=locations)


@app.route('/predict', methods=['POST'])
def predict():
    if 'user' not in session:
        return redirect(url_for('login'))

    location = request.form['location']
    sqft = float(request.form['sqft'])
    bhk = float(request.form['bhk'])
    bath = float(request.form['bath'])

    input_data = pd.DataFrame([[location, sqft, bhk, bath]],
                              columns=['location', 'total_sqft', 'size', 'bath'])

    prediction = model.predict(input_data)[0]
    prediction = round(prediction, 2)

    return render_template("result.html",
                           prediction=f"₹ {prediction:,}",
                           username=session['user'])


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT",5000))
    app.run(host='0.0.0.0',port=port)
