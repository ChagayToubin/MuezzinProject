from pathlib import Path
import datetime
import json
# from project.utilities.kafka.kafka_producer.kafka_pub import kafkaProducer


class Processing:
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
                  "Last modified":str(last_modified),
                  "Creation time":str(creation_time)
                  }
            return json.dumps(dic_info)
            # return dic_info

        except Exception as e:
            print(e)
    # @staticmethod
    # def send_to_kafka(kafka,json_file,topic):
    #     kafka.send_to_kapka(topic, json_file)
    #     kafka.close()









# st_size: Size of the file in bytes.
# st_mtime: Time of last modification (as a Unix timestamp).
# st_ctime: Time of last metadata change (creation time on some systems).
# st_atime: Time of last access.
# st_mode: File type and file system permissions.
# st_ino: Inode number.
# st_dev: Device ID.
# st_nlink: Number of hard links.
# st_uid: User ID of owner.
# st_gid: Group ID of owner.
