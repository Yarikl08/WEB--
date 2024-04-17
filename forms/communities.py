from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms import SubmitField
from wtforms.validators import DataRequired


class CommunitiesForm(FlaskForm):
    topic = StringField("����", validators=[DataRequired()])
    title = StringField("�������� ����������", validators=[DataRequired()])
    in_detail = TextAreaField("��������", validators=[DataRequired()])
    organizer = IntegerField("�����������", validators=[DataRequired()])
    members = StringField("���������", validators=[DataRequired()])
    contacts = StringField("��������", validators=[DataRequired()])
    submit = SubmitField('���������')