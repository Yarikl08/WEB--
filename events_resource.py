from flask import jsonify
from flask_restful import abort, Resource
from WEB_project_TуСОВКА_Igoshin_11_04_2024.data import db_session
from WEB_project_TуСОВКА_Igoshin_11_04_2024.data.events import Events
from WEB_project_TуСОВКА_Igoshin_11_04_2024.events_parser import parser


def events_not_found(event_id):
    session = db_session.create_session()
    events = session.query(Events).get(event_id)
    if not events:
        abort(404, message=f"Events {event_id} not found")


class EventResource(Resource):
    def get(self, event_id):
        events_not_found(event_id)
        session = db_session.create_session()
        events = session.query(Events).get(event_id)
        return jsonify({'events': events.to_dict(
            only=('id', 'topic', 'community', 'organizer', 'age_limit', 'area', 'start_date', 'end_date',
                  'is_finished'))})

    def put(self, event_id):
        args = parser.parse_args()
        events_not_found(event_id)
        session = db_session.create_session()
        events = {
            "topic": args['topic'],
            "community": args['community'],
            "organizer": args['organizer'],
            "age_limit": args['age_limit'],
            "area": args['area'],
            "start_date": args['start_date'],
            "end_date": args['end_date'],
            "is_finished": args['is_finished']
        }
        session.query(Events).filter(Events.id == event_id).update(events)
        session.commit()
        return jsonify({'success': 'OK'})

    def delete(self, event_id):
        events_not_found(event_id)
        session = db_session.create_session()
        events = session.query(Events).get(event_id)
        session.delete(events)
        session.commit()
        return jsonify({'success': 'OK'})


class EventsListResource(Resource):
    def get(self):
        session = db_session.create_session()
        events = session.query(Events).all()
        return jsonify({'events': [item.to_dict(
            only=('id', 'topic', 'community', 'organizer', 'age_limit', 'area', 'start_date', 'end_date',
                  'is_finished')) for item in events]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        events = Events(
            topic=args['topic'],
            community=args['community'],
            organizer=args['organizer'],
            age_limit=args['age_limit'],
            area=args['area'],
            start_date=args['start_date'],
            end_date=args['end_date'],
            is_finished = args['is_finished']
        )
        session.add(events)
        session.commit()
        return jsonify({'success': 'OK'})