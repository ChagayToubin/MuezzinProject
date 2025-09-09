import json
from project.utilities.transcription.transcriptions import Transcriptions


class Process:
    _folder_path=r"C:\Users\User\PycharmProjects\MuezzinProject07_09\project\data_files\podcasts"
    @staticmethod
    def get_data_from_kafka_and_send_elastic_and_mongo(kafka, es, mongo,folder_path):
        for i in kafka.consume():
            data_dict = json.loads(i.value)

            text=Transcriptions.voice_to_text(folder_path, data_dict["name"])
            data_dict["text"]=text
            print(data_dict)


            uniq_id = str(data_dict["size"]) + data_dict["name"]

            es.send_data(data_dict, uniq_id)

            mongo.send_audio(data_dict, uniq_id)


