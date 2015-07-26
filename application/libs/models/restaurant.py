from mongoengine import *


class Restaurant(Document):
	name = StringField()
	location = StringField(default="unknown")
	isOpen = BooleanField(default=False)
	totalTableNumber = IntField()
	tableLeft = IntField()
	tables = ListField(Table)

class Table(Document):
	restaurantName = StringField(required=True)
	capacity = IntField(required=True)
	occupied = IntField(default=0)
	status = StringField(default="empty")
	users = ListField(StringField(), default=[])
