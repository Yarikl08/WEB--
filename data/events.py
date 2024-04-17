import datetime

import sqlalchemy
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin

from WEB_project_TуСОВКА_Igoshin_11_04_2024.data.db_session import SqlAlchemyBase


# Модель Работы
class Events(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'events'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    topic = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    community = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    organizer = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    age_limit = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    area = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    start_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now())
    end_date = sqlalchemy.Column(sqlalchemy.DateTime)
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean, default=False)

    user = orm.relationship('User')

    def __repr__(self):
        return f"{self.topic} {self.community} {self.organizer} {self.age_limit} {self.area} {self.is_finished}"