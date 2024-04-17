from flask import jsonify
from flask_restful import abort, Resource
from WEB_project_TуСОВКА_Igoshin_11_04_2024.data import db_session
from WEB_project_TуСОВКА_Igoshin_11_04_2024.data.users import User
from WEB_project_TуСОВКА_Igoshin_11_04_2024.user_parser import parser


def user_not_found(user_id):
    session = db_session.create_session()
    user = session.query(User).get(user_id)
    if not user:
        abort(404, message=f"User {user_id} not found")


class UsersResource(Resource):
    def get(self, user_id):
        user_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        return jsonify({'user': user.to_dict(
            only=('surname', 'name', 'age', 'about_me', 'hobbies', 'city_from', 'phone'))})

    def delete(self, user_id):
        user_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        session.delete(user)
        session.commit()
        return jsonify({'success': 'OK'})

    def put(self, user_id):
        args = parser.parse_args()
        user_not_found(user_id)
        session = db_session.create_session()
        user = {
            "surname": args['surname'],
            "name": args['name'],
            "age": args['age'],
            "about_me": args['about_me'],
            "hobbies": args['hobbies'],
            "city_from": args['city_from'],
            "phone": args['phone']
        }
        session.query(User).filter(User.id == user_id).update(user)
        session.commit()
        return jsonify({'success': 'OK'})


class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({'users': [item.to_dict(
            only=('surname', 'name', 'age', 'about_me', 'hobbies', 'city_from', 'phone')) for item in users]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        user = User(
            surname=args['surname'],
            name=args['name'],
            age=args['age'],
            about_me=args['about_me'],
            hobbies=args['hobbies'],
            city_from=args['city_from'],
            phone = args['phone']
        )
        session.add(user)
        session.commit()
        return jsonify({'success': 'OK'})