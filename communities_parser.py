from flask_restful import reqparse


parser = reqparse.RequestParser()
parser.add_argument('topic', required=True)
parser.add_argument('title', required=True)
parser.add_argument('in_detail', required=True)
parser.add_argument('organizer', required=True, type=int)
parser.add_argument('members', required=True)
parser.add_argument('contacts', required=True)