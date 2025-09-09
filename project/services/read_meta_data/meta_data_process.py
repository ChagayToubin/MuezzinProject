from pathlib import Path
import datetime
import json


class Processing1:
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








