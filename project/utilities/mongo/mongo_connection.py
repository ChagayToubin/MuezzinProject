from pymongo import MongoClient
from project.config.settings import Settings

class Mongo:
    def __init__(self,host=None,user=None,password=None,db_name="muezzin"):
        self.host = host
        self.user = user
        self.password = password
        self.db_name =db_name
        self.client = None
        self.db = None

    def get_uri(self):

        if self.user and self.password:
            return f"mongodb+srv://{self.user}:{self.password}@{self.host}/{self.db_name}"
        else:
            print(f"mongodb://{self.host}:27017/{self.db_name}")
            return f"mongodb://{self.host}:27017/{self.db_name}"


    def connect(self):
        uri = self.get_uri()
        self.client = MongoClient(uri)
        self.db = self.client[self.db_name]
        # return self.db

    def close(self):
        if self.client:
            self.client.close()
            self.client = None
            self.db = None

    def create(self, collection_name , document):
        return self.db[collection_name].insert_one(document)
