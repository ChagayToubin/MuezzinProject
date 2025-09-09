
from elasticsearch import Elasticsearch
# from elasticsearch.helpers import  bulk
# from elasticsearch import helpers

class Elastic:
    def __init__(self, uri):

        self.host=uri[1]
        self.port=uri[0]
        self.uri = self.get_uri()

        self.index="muezzin_data_project"
        self.es = self.connection()

    def get_uri(self):
        if self.host and self.port:
            return f"http://{self.host}:{self.port}"
        else:
            return "http://localhost:9200"


    def connection(self):
        return Elasticsearch(self.uri)

    def close(self):
        if self.es:
            self.es.transport.close()
            self.es = None


    def init_es(self):
        mapping = self.init_mapping()
        if not self.es.indices.exists(index=self.index):
            self.es.indices.create(index=self.index, body=mapping)


    @staticmethod
    def init_mapping():
        mapping = {
            "mappings": {
                "properties": {
                    "name": {"type": "text"},
                    "size": {"type": "text"},
                    "Suffix": {"type": "text"},
                    "last_modified": {"type": "text"},
                    "creation_time": {"type": "text"},
                    "text": {"type": "text"}
                }
            }
        }
        return mapping

    def send_data(self,doc,uniq_id):
        w=self.es.index(index=self.index, id=uniq_id, body=doc)
        print(w)
        print("the data send")


