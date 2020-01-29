from flask import Blueprint, request, render_template

from tfteamaker.models import Post

main = Blueprint('main', __name__)


@main.route('/')
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=3)
    return render_template('home.html', page_title="Home", posts=posts)


@main.route('/about')
def about():
    return render_template('about.html', page_title="About")