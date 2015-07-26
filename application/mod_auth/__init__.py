from .. import manager
from ..libs.models.user import User

@manager.user_loader
def load_user(userid):
    querySet = User.objects(username = userid)
    return None if querySet.count() == 0 else querySet.first()