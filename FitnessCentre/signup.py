from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email, Length


class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('Логин', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Пароль', validators=[InputRequired(), Length(min=8, max=80)])
