from flask import Blueprint, flash, redirect, render_template, url_for, request, abort
from flask_login import login_required, current_user

from tfteamaker import db
from tfteamaker.models import Post
from tfteamaker.posts.forms import PostForm

posts = Blueprint('posts', __name__)


@posts.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        flash('Your post has been created', category='success')
        post = Post(title=form.title.data, content=form.content.data, author_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='New Post',
                           form=form, legend='New post')


@posts.route('/post/<int:post_id>')
def post(post_id):
    # post = Post.query.get(post_id)
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)

@login_required
@posts.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author_id != current_user.id:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has beed updated!', category='success')
        return redirect(url_for('posts.post', post_id=post_id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post',
                           form=form, legend='Update post')


@login_required
@posts.route('/post/<int:post_id>/delete', methods=['POST'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    post_title_to_delete = post.title
    if post.author_id != current_user.id:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash(f'Your post {post_title_to_delete} has beed deleted.', category='success')
    return redirect(url_for('main.home'))