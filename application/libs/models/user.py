from mongoengine import *
from check import Check
from restaurant import Restaurant

class User(Document):
	username = StringField(required=True, unique=True)
	name = StringField(required=True)
	email = StringField(required=True)
	password = StringField(required=True)
	def is_authenticated(self):
		return True
	def is_active(self):
		return True
	def is_anonymous(self):
		return True
	def get_id(self):
		return unicode(self.username)

class ResturantOwner(User):
	resturant = ReferenceField(Restaurant)

class Guest(User):
	checks = ListField(ReferenceField(Check))




