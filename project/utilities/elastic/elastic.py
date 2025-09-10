from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from elasticsearch import helpers


class Elastic:
    def __init__(self, uri):

        self.host = uri[1]
        self.port = uri[0]
        self.uri = self.get_uri()

        self.index = "muezzin_data_project_final"
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

    def send_data(self, doc, uniq_id):
        w = self.es.index(index=self.index, id=uniq_id, body=doc)
        print(w)
        print("the data send")

    def update_all_documents_sentiment(self):
        count_all = 0
        average = 0.30939176841270893

        scroll = self.es.search(
            index=self.index,
            scroll="2m",
            body={
                "_source": ["text"],
                "query": {"match_all": {}}

            }
        )

        scroll_id = scroll["_scroll_id"]
        hits = scroll["hits"]["hits"]

        while hits:
            actions = []
            for hit in hits:
                doc_id = hit["_id"]
                text = hit["_source"].get("text", "")
                count_number_of_words = (Elastic.count_words(text, ['Genocide', 'War Crimes', 'Apartheid', 'Massacre',
                                                                    'Nakba', 'Displacement', 'Humanitarian Crisis',
                                                                    'Blockade', 'Occupation', 'Refugees', 'ICC',
                                                                    'BDS']) * 2 +
                                         Elastic.count_words(text, ['Freedom Flotilla', 'Resistance', 'Liberation',
                                                                    'Free Palestine', 'Gaza', 'Ceasefire', 'Protest',
                                                                    'UNRWA']))

                if count_number_of_words == 0:
                    percent = 0
                else:
                    percent = (count_number_of_words / len(text)) * 100

                is_bds = percent > average
                bds_threat_level = Elastic.bds_threat_level_calculation(percent, average)

                count_all += ((count_number_of_words / len(text)) * 100)

                actions.append({
                    "_op_type": "update",
                    "_index": self.index,
                    "_id": doc_id,
                    "doc": {"bds_precent": percent, "is_bds": is_bds, "bds_threat_level": bds_threat_level}

                })

            if actions:
                success = bulk(self.es, actions)
                print(f"Updated {success} docs")

            scroll = self.es.scroll(scroll_id=scroll_id, scroll="2m")
            scroll_id = scroll["_scroll_id"]
            hits = scroll["hits"]["hits"]
            # print(count_all/34)

    @staticmethod
    def count_words(text, bad_words):
        count = 0
        for i in text.split():
            if i in bad_words:
                count += 1

        return count

    @staticmethod
    def bds_threat_level_calculation(percent, average):

        if percent > average:
            return "high"
        elif percent <= 0:
            return "none"
        else:
            return "medium"

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
                    "text": {"type": "keyword"}
                }
            }
        }
        return mapping


    def find_risk(self,level_risk):

        query = {
            "query": {
                "bool": {
                    "must": [
                        {"term": {"bds_threat_level": level_risk}}

                    ]
                }
            }
        }
        response = self.es.search(index=self.index, body=query)
        hits = response["hits"]["hits"]
        if not hits:
            return {"message": "לא נמצאו מסמכים מתאימים"}
        return hits
