import json
from elasticsearch.helpers import scan, bulk
from elasticsearch import helpers

class Process2:
    @staticmethod
    def get_data_from_kafka(kafka):
        for i in kafka.consume():
            data_dict = json.loads(i.value)
            print(data_dict)
    @staticmethod
    def send_to_elastic(es):
        mapping = es.init_mapping("xz")
        # if not self.es.indices.exists(index=self.index):
        #     self.es.indices.create(index=self.index, body=mapping)
        actions = []
        for i, doc in enumerate("s"):
            document = {
                "text": doc["text"],
                "TweetID": str(doc["TweetID"]),
                "CreateDate": str(doc["CreateDate"]),
                "Antisemitic": doc["Antisemitic"]

            }

            actions.append({
                "_index": es.index,
                "_id": i,
                "_source": document
            })

        helpers.bulk(es.es, actions)
        print(f"Indexed {len(actions)} documents.")

        pass
    def init_mapping(self, index_name):
        self.index = index_name
        mapping = {
            "mappings": {
                "properties": {
                    "text": {"type": "text"},
                    "TweetID": {"type": "keyword"},
                    "CreateDate": {"type": "text"},
                    "Antisemitic": {"type": "integer"},
                    "sentiment": {"type": "keyword"},
                    "weapons": {"type": "keyword"}
                }
            }
        }
        return mapping
