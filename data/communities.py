import sqlalchemy
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin

from WEB_project_TуСОВКА_Igoshin_11_04_2024.data.db_session import SqlAlchemyBase


# Модель Работы
class Communities(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'communities'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    topic = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    in_detail = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    organizer = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    members = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    contacts = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    user = orm.relationship('User')