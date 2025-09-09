from pathlib import Path
import datetime
import json


# Used for the processes running in the service

class Processing:
    # The function receives a file path and retrieves all the information about it.
    @staticmethod
    def read_meta_data(path_file):
        try:
            file_path = Path(path_file)
            stats = file_path.stat()
            file_name = file_path.name
            size=stats.st_size
            ending=file_path.suffix
            creation_time = datetime.datetime.fromtimestamp(stats.st_ctime)
            last_modified=datetime.datetime.fromtimestamp(stats.st_mtime)


            dic_info={"name":file_name,
                  "size":size,
                  "Suffix":ending,
                  "last_modified":str(last_modified),
                  "creation_time":str(creation_time)
                  }
            return json.dumps(dic_info)

        except Exception as e:
            print(e)

    # The function receives a folder path, a Kafka object,
    # and a subject,
    # and iterates over the files and sends them to Kafka.
    @staticmethod
    def send_kafka(path_folder,kafka,topic):
        kafka.open()

        for file_path in path_folder.iterdir():
            if file_path.is_file():
                metadata = Processing.read_meta_data(file_path)
                kafka.send_to_kafka(topic, metadata)
        kafka.close()










