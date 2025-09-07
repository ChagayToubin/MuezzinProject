from project.services.processing_receving.processing_receving_process import Process2
from project.utilities.kafka.kafka_consumer.kafka_sub import MyKafkaConsumer
class Manager:
    def __init__(self,topic,kafka_config,uri_es):
        self.kafka=MyKafkaConsumer(topic,kafka_config)
        # self.es
        self.processing=Process2()

    def app(self):

        self.kafka.open()
        self.processing.get_data_from_kafka(self.kafka)


