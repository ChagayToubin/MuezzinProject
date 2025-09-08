
from project.services.processing_receving.processing_receving_process import Process2
from project.utilities.kafka.kafka_consumer.kafka_sub import MyKafkaConsumer
from project.utilities.elastic.elastic_connection import Elastic
from project.utilities.mongo.mongo_connection import Mongo
from project.utilities.elastic.logger_info import Logger
class Manager:
    def __init__(self,topic,kafka_config,uri_es,):
        self.folder_path=r"C:\Users\User\PycharmProjects\MuezzinProject07_09\project\data_files\podcasts"

        self.kafka=MyKafkaConsumer(topic,kafka_config)

        self.elastic=Elastic(uri_es)

        self.mongo=Mongo()

        self.processing=Process2()

    def app(self):

        self.mongo.connect()

        self.kafka.open()


        self.elastic.init_es()

        self.processing.get_data_from_kafka_and_send_elastic_and_mongo(self.kafka,self.elastic,self.mongo,self.folder_path)


