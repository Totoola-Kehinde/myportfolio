from schematics.models import Model
from bson.objectid import ObjectId
import datetime

class wiseword(Model):
    """ Collection Of the wisewords from users """

    def __init__(self, wiseword_id, wiseword, anonymous, user):
        if wiseword_id == None:
            self._id = ObjectId()

        self.user = user
        self.anonymous = anonymous
        self.wiseword = wiseword
        self.daytime = datetime.datetime.utcnow()

    def get_as_dict(self):

        return self.__dict__
