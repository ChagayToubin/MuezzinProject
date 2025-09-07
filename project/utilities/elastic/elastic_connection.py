
from elasticsearch import Elasticsearch


class Elastic:
    def __init__(self, uri):
        self.uri = self.get_uri(uri)
        self.client = None

    def get_uri(self,usr=None):
        if usr:
            return f"http://{usr}:9200"
        else:
            return "http://localhost:9200"


    def connect(self):
        if not self.client:
            self.client = Elasticsearch(self.uri)
        return self.client

    def close(self):
        if self.client:
            self.client.transport.close()
            self.client = None
