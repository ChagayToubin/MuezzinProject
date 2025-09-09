from project.services.read_meta_data.meta_data_process import Processing
from project.utilities.kafka.kafka_producer.kafka_pub import Producer
from project.utilities.logger.logger_info import Logger
from pathlib import Path

logger = Logger.get_logger()

class Manager:
    def __init__(self, kafka_config, path_file, topic):

        # Initialize all objects used in this service.
        try:

            self.process_meta_data = Processing()

            self.path_folder = Path(path_file)

            self.kafka = Producer(kafka_config)

            self.topic = topic

            logger.info("Reading the metadata and sending it to Kefka was successful.")
        except Exception as e:
            logger.error(f"Reading the metadata and sending it to Kefka was faild becuas{e}")

    def app(self):
        # Runs the service logic

        try:
            self.process_meta_data.send_kafka(
                self.path_folder, self.kafka, self.topic)

            logger.info("Reading the metadata and sending it to Kefka was successful.")
        except Exception as e:
            logger.error(f"Reading the metadata and sending it to Kefka failed because:{e}")

