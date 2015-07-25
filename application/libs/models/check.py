from mongoengine import *
import datetime

class Check(Document):
	resturantName = StringField(required=True)
	tableId = StringField(required=True)
	amount = StringField(required=True)
	paymentId = StringField()
	paymentType = StringField(default="dollar")
	createTime = DateTimeField(default=datetime.datetime.now)

