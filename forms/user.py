from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, EmailField, IntegerField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    login_email = EmailField('����� / �����', validators=[DataRequired()])
    password = PasswordField('������', validators=[DataRequired()])
    repeat_password = PasswordField('��������� ������', validators=[DataRequired()])
    surname = StringField('�������', validators=[DataRequired()])
    name = StringField('���', validators=[DataRequired()])
    age = IntegerField('�������')
    about_me = TextAreaField('������� � ����')
    hobbies = StringField('�����')
    city_from = StringField('��� �����?')
    phone = StringField("�������")
    submit = SubmitField('���������')