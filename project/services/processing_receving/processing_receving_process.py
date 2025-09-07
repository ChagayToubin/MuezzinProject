import json


class Process2:
    @staticmethod
    def get_data_from_kafka(kafka):
        for i in kafka.consume():
            data_dict = json.loads(i.value)
            print(data_dict.keys())
    @staticmethod
    def send_to_elastic(es):
        pass
