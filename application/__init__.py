from flask import Flask, request
from mongoengine import connect, register_connection
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('config')
connect(app.config['DATABASE'])
manager = LoginManager()
manager.init_app(app)

from mod_auth.controllers import mod_auth
app.register_blueprint(mod_auth)


@app.route("/", methods=["GET"])
def root():
	return "hello world", 200




