from flask import Flask
from monogengine import connect, register_connection

app = Flask(__name__)
app.config.from_object('config')

connect(app.config['MONGO_DATABASE'])




