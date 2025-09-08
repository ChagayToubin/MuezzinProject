import json

class Process2:
    @staticmethod
    def get_data_from_kafka_and_send_elastic_and_mongo(kafka,es,mongo):

        for i in kafka.consume():
            data_dict = json.loads(i.value)
            uniq_id=str(data_dict["size"])+data_dict["name"]

            es.send_data(data_dict,uniq_id)
            mongo.send_audio(data_dict,uniq_id)



# {'name': 'download (3).wav', 'size': 2076090, 'Suffix': '.wav', 'last_modified': '2025-09-07 10:39:18.403126', 'creation_time': '2025-09-07 11:06:01.330065'}
