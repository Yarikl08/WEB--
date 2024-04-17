from flask import jsonify
from flask_restful import abort, Resource
from WEB_project_TуСОВКА_Igoshin_11_04_2024.communities_parser import parser
from WEB_project_TуСОВКА_Igoshin_11_04_2024.data import db_session
from WEB_project_TуСОВКА_Igoshin_11_04_2024.data.communities import Communities


def communities_not_found(communities_id):
    session = db_session.create_session()
    communities = session.query(Communities).get(communities_id)
    if not communities:
        abort(404, message=f"Communities {communities_id} not found")


class CommunitiesResource(Resource):
    def get(self, communities_id):
        communities_not_found(communities_id)
        session = db_session.create_session()
        communities = session.query(Communities).get(communities_id)
        return jsonify({'communities': communities.to_dict(
            only=('id', 'topic', 'title', 'in_detail', 'organizer', 'members', 'contacts'))})

    def put(self, communities_id):
        args = parser.parse_args()
        communities_not_found(communities_id)
        session = db_session.create_session()
        communities = {
            "topic": args['topic'],
            "title": args['title'],
            "in_detail": args['in_detail'],
            "organizer": args['organizer'],
            "members": args['members'],
            "contacts": args['contacts']
        }
        session.query(Communities).filter(Communities.id == communities_id).update(communities)
        session.commit()
        return jsonify({'success': 'OK'})

    def delete(self, communities_id):
        communities_not_found(communities_id)
        session = db_session.create_session()
        communities = session.query(Communities).get(communities_id)
        session.delete(communities)
        session.commit()
        return jsonify({'success': 'OK'})


class CommunitiesListResource(Resource):
    def get(self):
        session = db_session.create_session()
        communities = session.query(Communities).all()
        return jsonify({'communities': [item.to_dict(
            only=('id', 'topic', 'title', 'in_detail', 'organizer', 'members', 'contacts')) for item in communities]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        communities = Communities(
            topic=args['topic'],
            title=args['title'],
            in_detail=args['in_detail'],
            organizer=args['organizer'],
            members=args['members'],
            contacts=args['contacts']
        )
        session.add(communities)
        session.commit()
        return jsonify({'success': 'OK'})