from flask_wtf import FlaskForm
from wtforms import BooleanField
from wtforms import StringField, PasswordField, SelectField, IntegerField
from wtforms.validators import InputRequired, Length


class EditForm(FlaskForm):
    name = StringField('Имя', validators=[InputRequired(), Length(min=2)])
    surname = StringField('Фамилия', validators=[InputRequired(), Length(min=2)])
    midname = StringField('Отчество', validators=[InputRequired(), Length(min=2)])
    username = StringField('Логин', validators=[InputRequired(), Length(min=4, max=25)])
    ticket = StringField('Номер абонемента', validators=[Length(min=0, max=20)])
    enddate = StringField('Время окончания действия абонемента', validators=[Length(min=0, max=20)])
    lvl = StringField('Уровень пользователя', validators=[InputRequired(), Length(min=0)])

