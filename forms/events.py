from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


class EventsForm(FlaskForm):
    topic = StringField("����", validators=[DataRequired()])
    community = StringField("�������� �����������", validators=[DataRequired()])
    organizer = IntegerField("�����������")
    age_limit = IntegerField("���������� ����������� (+)")
    area = StringField("��������")
    start_date = DateField("������")
    end_date = DateField("���������")
    is_finished = BooleanField("���������?")
    submit = SubmitField('���������')