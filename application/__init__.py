from flask import Flask, request
from mongoengine import connect, register_connection

app = Flask(__name__)
app.config.from_object('config')
connect(app.config['DATABASE'])

from mod_auth.controllers import mod_auth
app.register_blueprint(mod_auth)

@app.route("/", methods=["GET"])
def root():
	return "hello world", 200




