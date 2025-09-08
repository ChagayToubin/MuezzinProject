from copyreg import dispatch_table

from project.services.processing_receving.processing_receving_process import Process2
from project.utilities.kafka.kafka_consumer.kafka_sub import MyKafkaConsumer
from project.utilities.elastic.elastic_connection import Elastic
class Manager:
    def __init__(self,topic,kafka_config,uri_es):
        self.kafka=MyKafkaConsumer(topic,kafka_config)

        self.elastic=Elastic(uri_es)

        self.processing=Process2()

    def app(self):

        self.kafka.open()


        self.elastic.init_es()

        self.processing.get_data_from_kafka_and_send_elastic_and_mongo(self.kafka,self.elastic)


