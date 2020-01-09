from flask import Flask, render_template, url_for, flash, redirect, get_flashed_messages
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '990331fc1d4147989e698699937f0160'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User(#{self.id}, '{self.username}', '{self.email}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(40), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Post({self.title}, {self.date_posted})"


posts = [
    {
        'author': 'Dominik Szymkowiak',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'January 9, 2020'
    },
    {
        'author': 'Wojtek Wojewodzic',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'January 10, 2019'
    },
    {
        'author': 'Krystian Zelech',
        'title': 'Blog Post 3',
        'content': 'Third post content',
        'date_posted': 'January 11, 2020'
    }

]


@app.route('/')
def home():
    return render_template('home.html', page_title="Home", posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', page_title="About")


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(message=f'Account created for {form.username.data}! Let the TeaMaking begin!', category='info')
        return redirect(url_for('home'))
    return render_template('register.html', page_title="Register", form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(message=f"Welcome back {form.username.data}!", category='success')
        return redirect(url_for('home'))
    else:
        flash('Login unsuccessful. Please check username and password', category='danger')
    return render_template('login.html', page_title="Login", form=form)


if __name__ == '__main__':
    app.run(debug=True)
