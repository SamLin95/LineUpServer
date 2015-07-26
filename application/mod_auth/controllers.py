from flask import Blueprint, request
from ..libs.models.user import User
from flask_login import login_user, logout_user
from parsers import auth_parser, sign_up_parser
from mongoengine import NotUniqueError

mod_auth = Blueprint("auth", __name__, url_prefix="/auth")

@mod_auth.route("/login", methods=["GET"])
def login():
    req = auth_parser.parse_args(strict=True)
    username = req.get("username")
    pw = req.get("password")
    quert_set = User.objects(username = username, password = pw)
    if quert_set.count() == 0:
        return "Login Failed", 400
    else:
        login_user(quert_set.first())
        return "Login Successfull", 200

@mod_auth.route("/signup", methods=["POST"])
def signup():
    req = sign_up_parser.parse_args(strict=True)
    print req.get("username")
    try:
        new_user = User(username=req.get("username"),
                        password = req.get("password"),
                        email = req.get("email"),
                        name = req.get("name"))
        new_user.save()
        return "signed up", 200
    except NotUniqueError as e:
        return str(e), 400

@mod_auth.route("/logout", methods=["POST"])
def logout():
    logout_user()
    return "Logged Out", 200





