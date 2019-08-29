from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired


class LoginForm(FlaskForm):
    username = StringField('Username', [InputRequired()])
    password = PasswordField('Password', [InputRequired()])
    remember_me = BooleanField('Mantenha-me conectado')


class RegisterForm(FlaskForm):
    username = StringField('Matricula', [InputRequired()])
    email = StringField('Email', [InputRequired()])
    sector = StringField('Setor', [InputRequired()])
    password_hash = PasswordField('Password', [InputRequired()])
    confirm_password = PasswordField('Password', [InputRequired()])
    super_admin = BooleanField('Administrador')
