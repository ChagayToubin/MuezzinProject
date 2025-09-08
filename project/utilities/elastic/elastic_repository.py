class ElasticRepository:
    @staticmethod
    def insert(client, index_name, doc_id, doc):
        return client.index(index=index_name, id=doc_id, document=doc)

