import os

from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.utils import secure_filename

from app import app, db, login_manager
from forms import VideoUploadForm, LoginForm, SignupForm
from models import User, Video


@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(userid))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/tags')
def tags():
    return render_template('tags.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    # Create a new BookmarkForm instance.
    form = VideoUploadForm()
    # Validate the form, store the bookmarks and redirect to the index.
    if form.validate_on_submit():
        url = form.url.data
        description = form.description.data
        filename = secure_filename(form.file.data.filename)
        root_dir = os.path.dirname(app.instance_path)
        form.file.data.save(os.path.join('static/uploads', filename))
        filepath = os.path.join(root_dir, 'static/uploads', filename)
        uservideo = Video(user=current_user, url=url, description=description, file_path=filepath)
        db.session.add(uservideo)
        db.session.commit()
        flash("Thank's for submitting'{}', we'll review it and let you know when it's published.".format(description))
        return redirect(url_for('index'))
    # Render the add template giving it the empty form object.
    return render_template('add.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    # Create a new LoginForm FlaskForm instance from the forms.py
    form = LoginForm()
    # Validate the form, store the bookmarks and redirect to the index.
    if form.validate_on_submit():
        # Login and validate the user
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None:
            # Pass the user object and remember_me flag and register it with Flask-Login
            login_user(user, form.remember_me.data)
            flash("Logged in successfully as {}.".format(user.username))
            # Redirect to the index page or the page the user was trying to access pulled from the next arg.
            return redirect(request.args.get('next') or url_for('index'))
        flash("Sorry, incorrect username or password. Please try again.")
    return render_template('login.html', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        # ToDo: Change user variable names so there's no warning. Even though they're scope safe.
        new_user = User(email=form.email.data,
                        username=form.username.data,
                        password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash("Welcome to Thermos {}! Please login with the details you provided".format(new_user.username))
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


# Error handling.
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500
