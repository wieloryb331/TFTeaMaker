from flask import Flask, render_template, url_for, flash, redirect, get_flashed_messages
from forms import RegistrationForm, LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = '990331fc1d4147989e698699937f0160'

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
        flash(message=f'Account created for {form.username.data}! Let the TeaMaking begin!', category='success')
        return redirect(url_for('home'))
    return render_template('register.html', page_title="Register", form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', page_title="Login", form=form)


if __name__ == '__main__':
    app.run(debug=True)
