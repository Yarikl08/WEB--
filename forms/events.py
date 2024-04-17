from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


class EventsForm(FlaskForm):
    topic = StringField("Тема", validators=[DataRequired()])
    community = StringField("Название мероприятия", validators=[DataRequired()])
    organizer = IntegerField("Организатор")
    age_limit = IntegerField("Возрастное ограничение (+)")
    area = StringField("Площадка")
    start_date = DateField("Начало")
    end_date = DateField("Окончание")
    is_finished = BooleanField("Закончено?")
    submit = SubmitField('Сохранить')