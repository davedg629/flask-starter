from app import app, db
from flask import Flask, flash, redirect, render_template, request, \
    session, url_for, g
from functools import wraps
from app.forms import SampleForm, LoginForm
from app.models import Item


def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the {} field - {}".format(
                getattr(form, field).label.text,
                error
            ), 'error')


def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('Please login.')
            return redirect(url_for('login'))
    return wrap


@app.errorhandler(404)
def page_not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if 'logged_in' in session:
        return redirect(url_for('admin'))
    form = LoginForm()
    error = None
    if form.validate_on_submit():
        if request.form['username'] == app.config['ADMIN_USERNAME'] and \
                request.form['password'] == app.config['ADMIN_PASSWORD']:
            session['logged_in'] = True
            flash('Login successful.')
            return redirect(url_for('admin'))
        else:
            error = 'Invalid username or password.'
    return render_template('login.html',
                           title="Login", form=form, error=error)


@app.route('/logout/')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You have been logged out.')
    return redirect(url_for('index'))


@app.route('/admin/')
@login_required
def admin():
    return render_template('admin.html',
                           title="Dashboard")


@app.route('/')
def index():
    welcome = 'Hello World!'
    return render_template('index.html', welcome=welcome)
