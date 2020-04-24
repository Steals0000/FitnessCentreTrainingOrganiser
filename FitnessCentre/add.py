from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email, Length


class AddForm(FlaskForm):
    name = StringField('Имя', validators=[InputRequired(),  Length(min=2)])
    surname = StringField('Фамилия', validators=[InputRequired(),  Length(min=2)])
    midname = StringField('Отчество', validators=[InputRequired(),  Length(min=2)])
    username = StringField('Логин', validators=[InputRequired(), Length(min=4, max=25)])
    password = PasswordField('Пароль', validators=[InputRequired(), Length(min=8, max=80)])
    ticket = StringField('Номер абонемента', validators=[Length(min=0, max=20)])
    enddate = StringField('Время окончания действия абонемента', validators=[Length(min=0, max=20)])

