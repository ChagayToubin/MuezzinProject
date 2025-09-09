
from project.services.Receiving_processing_data.data_processing import Process
from project.utilities.kafka.kafka_consumer.kafka_sub import MyKafkaConsumer
from project.utilities.elastic.elastic import Elastic
from project.utilities.mongo.mongo import Mongo
class Manager:
    def __init__(self,topic,kafka_config,uri_es,mong_setting):
        self.folder_path=r"C:\Users\User\PycharmProjects\MuezzinProject07_09\project\data_files\podcasts"

        self.kafka=MyKafkaConsumer(topic,kafka_config)

        self.elastic=Elastic(uri_es)

        self.mongo=Mongo(mong_setting)

        self.processing=Process()

    def app(self):

        self.mongo.connect()

        self.kafka.open()

        self.elastic.init_es()

        self.processing.get_data_from_kafka_and_send_elastic_and_mongo(self.kafka,self.elastic,self.mongo,self.folder_path)


