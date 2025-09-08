import os
from sys import path_hooks

import gridfs
from pymongo import MongoClient
from datetime import datetime


class Mongo:
    def __init__(self):

        self.host = os.getenv("MONGO_HOST", "localhost")
        self.port = int(os.getenv("MONGO_PORT", 27017))
        self.db_name = os.getenv("MONGO_DB", "test_db")
        self.user = os.getenv("MONGO_USER",None)
        self.password = os.getenv("MONGO_PASS",None)

        self.client = None
        self.db = None

    def get_uri(self):
        """יוצר URI מתוך משתני הסביבה"""
        # if self.user and self.password:
        #     return f"mongodb://{self.user}:{self.password}@{self.host}:{self.port}/{self.db_name}"
        return "mongodb://localhost:27017/"


    def connect(self):
        """פותח חיבור למסד"""
        uri = self.get_uri()
        self.client = MongoClient(uri)
        self.db = self.client[self.db_name]
        print(f"connected ")

    def close(self):

        if self.client:
            self.client.close()
            self.client = None
            self.db = None
            print("Connection closed")

    def create(self, collection_name, document):

        return self.db[collection_name].insert_one(document)

    def read_all(self, collection_name):

        return list(self.db[collection_name].find())

    def send_audio(self,data_dict,uniq_id):
        fs = gridfs.GridFS(self.db)
        print(data_dict["name"])
        path_folder = r"C:\Users\User\PycharmProjects\MuezzinProject07_09\project\data_files\podcasts"

        audio_file_path = f"{path_folder}/{data_dict["name"]}"
        with open(audio_file_path, "rb") as audio_file:
            file_id = fs.put(audio_file, filename=uniq_id)
            print(file_id)

