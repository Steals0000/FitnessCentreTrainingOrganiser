from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email, Length


class RegisterForm(FlaskForm):
    name = StringField('Имя', validators=[InputRequired(),  Length(min=2)])
    surname = StringField('Фамилия', validators=[InputRequired(),  Length(min=2)])
    midname = StringField('Отчество', validators=[InputRequired(),  Length(min=2)])
    username = StringField('Логин', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Пароль', validators=[InputRequired(), Length(min=8, max=80)])
