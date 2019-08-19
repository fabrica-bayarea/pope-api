from flask_wtf import FlaskForm
from wtforms import StringField,  BooleanField
from wtforms.validators import InputRequired


class OrganizationForm(FlaskForm):
    name = StringField('Nome', [InputRequired()])
    tell = StringField('Telefone', [InputRequired()])
    email = StringField('Email', [InputRequired()])
    address = StringField('Endereço', [InputRequired()])
    city = StringField('Cidade', [InputRequired()])
    description = StringField('Descrição', [InputRequired()])
    free = BooleanField('Grátis')
    id_area = StringField('Area', [InputRequired()])
    id_sub_area = StringField('Sub Area', [InputRequired()])
    id_attendance = StringField('Atendimento', [InputRequired()])
