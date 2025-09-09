from project.utilities.elastic.elastic import Elastic
class Manager:
    def __init__(self,uri_es):
        self.elastic=Elastic(uri_es)

    def app(self):
        self.elastic.update_all_documents_sentiment()
