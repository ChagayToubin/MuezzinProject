from project.services.read_meta_data.meta_data_process import Processing
from project.utilities.kafka.kafka_producer.kafka_pub import Producer
class Manager:
    def __init__(self,kafka_config,path_file):
        self.process_meta_data=Processing()
        self.path_file=path_file
        self.kafka=Producer(kafka_config)


    def app(self):

        metadata=self.process_meta_data.read_meta_data(self.path_file)
        self.kafka.open()
        self.kafka.send_to_kafka("MetaData",metadata)
        self.kafka.close()



