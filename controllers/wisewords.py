import pymongo
from pymongo import MongoClient
from models.wiseword import wiseword
from bson.objectid import ObjectId
import settings

class wisewords(wiseword):
    """ wisewords Controller inherits the wiseword model used in writing and reading from MongoDB """

    error_msg = None
    
    def __init__(self):
        self.client =  MongoClient(settings.MONGODB_URI)
        self.db =  self.client[settings.MONGODB_DATABASE]

    def create(self, wiseword):
        if wiseword is not None:
            try:
                return self.db.wisewords.insert_one(wiseword.get_as_dict())
            except pymongo.errors.NetworkTimeout as e:
                self.error_msg = "Error :{}".format(e)
                return self.error_msg
        else:
            return Exception("Nothing to save, because wiseword parameter is None")

    def read(self, id=None): 
        if id is None:
            try:
                return self.db.wisewords.find({})
            except pymongo.errors.NetworkTimeout as e:
                self.error_msg = "Error :{}".format(e)
                return self.error_msg
        else:
            try:
                return self.db.wisewords.find({"_id":ObjectId(id)})
            except pymongo.errors.NetworkTimeout as e:
                self.error_msg = "Error :{}".format(e)
                return self.error_msg