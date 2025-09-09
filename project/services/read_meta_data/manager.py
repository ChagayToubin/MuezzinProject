from project.services.read_meta_data.meta_data_process import Processing
from project.utilities.kafka.kafka_producer.kafka_pub import Producer
from pathlib import Path


class Manager:
    def __init__(self, kafka_config, path_file, topic):
        # Initialize all objects used in this service.
        self.process_meta_data = Processing()
        self.path_folder = Path(path_file)
        self.kafka = Producer(kafka_config)
        self.topic = topic

    def app(self):
        # Runs the service logic

        self.process_meta_data.send_kafka(
            self.path_folder, self.kafka, self.topic)
