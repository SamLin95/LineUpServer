__author__ = 'slin'
from flask_restful import reqparse, request

auth_parser = reqparse.RequestParser()
auth_parser.add_argument("username", type=str)
auth_parser.add_argument("password", type=str)

sign_up_parser = reqparse.RequestParser()
sign_up_parser.add_argument("username", type=str)
sign_up_parser.add_argument("password", type=str)
sign_up_parser.add_argument("email", type=str)
sign_up_parser.add_argument("name", type=str)

