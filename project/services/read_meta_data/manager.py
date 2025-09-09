from project.services.read_meta_data.meta_data_process import Processing1
from project.utilities.kafka.kafka_producer.kafka_pub import Producer
from pathlib import Path
class Manager:
    def __init__(self,kafka_config,path_file,topic):
        self.process_meta_data=Processing1()
        self.path_folder=Path(path_file)
        self.kafka=Producer(kafka_config)
        self.topic=topic


    def app(self):
        self.kafka.open()
        for file_path in self.path_folder.iterdir():
            if file_path.is_file():
                metadata=self.process_meta_data.read_meta_data(file_path)
                self.kafka.send_to_kafka(self.topic,metadata)

        self.kafka.close()




