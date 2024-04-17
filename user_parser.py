from flask_restful import reqparse


parser = reqparse.RequestParser()
parser.add_argument('surname', required=True)
parser.add_argument('name', required=True)
parser.add_argument('age', required=True, type=int)
parser.add_argument('about_me', required=True)
parser.add_argument('hobbies', required=True)
parser.add_argument('city_from', required=True)
parser.add_argument('phone', required=True)