# -*- coding: utf-8 -*-

from main import app
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired



app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://flask:plop@localhost/test-flask'
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = "HolyEmmanuelISellassieIJahRastafari"
# app.config['WTF_CSRF_SECRET_KEY'] ="HolyEmmanuelISellassieIJahRastafari"


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    avatar = db.Column(db.String(500))

    def __repr__(self):
        return '<User %s %s>' %(self.first_name, self.first_name)

# images = UploadSet('images', IMAGES)

class MyForm(FlaskForm):
    first_name_input = StringField('', validators=[DataRequired()])
    last_name_input = StringField('', validators=[DataRequired()])
    email_input = StringField('', validators=[DataRequired()])
    avatar_input = FileField('', validators=[FileRequired()])
