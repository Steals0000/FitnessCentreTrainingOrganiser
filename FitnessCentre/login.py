from flask_wtf import FlaskForm
from wtforms import BooleanField
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Пароль', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')
