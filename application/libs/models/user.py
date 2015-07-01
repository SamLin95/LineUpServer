from mongoengine import *
from check import Check
from restaurant import Restaurant

class User(Document):
	username = StringField(required=True, unique=True)
	name = StringField(required=True)
	email = StringField(required=True)

class ResturantOwner(User):
	resturant = ReferencedField(Restaurant)

class Guest(User):
	checks = ListField(ReferencedField(Check))
