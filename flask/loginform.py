from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username_avs = StringField('id астронавта', validators=[DataRequired()])
    password_avs = PasswordField('Пароль астронавта', validators=[DataRequired()])
    username_com = StringField('id капитана', validators=[DataRequired()])
    password_com = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')