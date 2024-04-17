from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms import SubmitField
from wtforms.validators import DataRequired


class CommunitiesForm(FlaskForm):
    topic = StringField("Тема", validators=[DataRequired()])
    title = StringField("Название сообщества", validators=[DataRequired()])
    in_detail = TextAreaField("Описание", validators=[DataRequired()])
    organizer = IntegerField("Организатор", validators=[DataRequired()])
    members = StringField("Участники", validators=[DataRequired()])
    contacts = StringField("Контакты", validators=[DataRequired()])
    submit = SubmitField('Сохранить')