import datetime
from flask_restful import reqparse


parser = reqparse.RequestParser()
parser.add_argument('topic', required=True)
parser.add_argument('community', required=True)
parser.add_argument('organizer', required=True, type=int)
parser.add_argument('age_limit', required=True, type=int)
parser.add_argument('area', required=True)
parser.add_argument('start_date', required=True, type=datetime.datetime)
parser.add_argument('end_date', required=True, type=datetime.datetime)
parser.add_argument('is_finished', required=True, type=bool)