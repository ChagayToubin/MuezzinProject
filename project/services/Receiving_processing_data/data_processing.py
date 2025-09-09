import json
from project.utilities.transcription.transcriptions import Transcriptions


# Used for the processes running in the service

class Process:
    _folder_path = r"C:\Users\User\PycharmProjects\MuezzinProject07_09\project\data_files\podcasts"

    # The function receives :
    # a Kafka object, an Elastic object, a Mongo object,
    # and a directory where the files are located.
    # The function pulls information from Kafka, transcribes the information,
    # and sends it to Mongo and Elastic accordingly.
    @staticmethod
    def get_data_send_m_es(kafka, es, mongo, folder_path):
        for i in kafka.consume():
            data_dict = json.loads(i.value)

            text = Transcriptions.voice_to_text(folder_path, data_dict["name"])
            data_dict["text"] = text
            print(data_dict)
            uniq_id = str(data_dict["size"]) + data_dict["name"]
            es.send_data(data_dict, uniq_id)

            mongo.send_audio(data_dict, uniq_id)
