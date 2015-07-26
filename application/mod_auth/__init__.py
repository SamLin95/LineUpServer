from .. import manager

@manager.user_loader
def load_user(userid):
    querySet = User.objects(username = userid)
    return None if querySet.count() == 0 else querySet.first()