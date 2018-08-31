# -*- coding: utf-8 -*-

import os
from flask import url_for, render_template, redirect
from models import User
from models import MyForm, db
from app import app, csrf
from werkzeug.utils import secure_filename


@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users = users)


@app.route("/account/<username>")
def userpage(username):
    users = User.query.all()
    user = User.query.filter_by( username = username ).first()
    return render_template('user.html', user = user, users = users)


@app.route("/contact")
def contactpage():
    users = User.query.all()
    return render_template('contact.html', users = users)


@app.route('/suscribe', methods=['GET', 'POST'])
def suscribe():
    users = User.query.all()
    form = MyForm()
    if form.validate_on_submit():
        first_name_input = form.first_name_input.data
        last_name_input = form.last_name_input.data
        username_generated = first_name_input.lower() +'-'+last_name_input.lower()
        email_input = form.email_input.data
        avatar_input = form.avatar_input.data
        filename = secure_filename(avatar_input.filename)
        avatar_input.save(os.path.join(
            app.instance_path, 'photos', filename
        ))
        filepath = "/instance/photos/" + filename
        user = User(username = username_generated, first_name = first_name_input.lower(), last_name = last_name_input.lower(), email = email_input.lower(), avatar = filepath)
        db.session.add(user)
        db.session.commit()
        redirect(url_for('index', users = users))
    return render_template('suscribe.html', form = form, users = users)
