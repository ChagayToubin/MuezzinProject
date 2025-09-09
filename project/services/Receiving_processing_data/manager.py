
from project.services.Receiving_processing_data.data_processing import Process
from project.utilities.kafka.kafka_consumer.kafka_sub import MyKafkaConsumer
from project.utilities.elastic.elastic import Elastic
from project.utilities.mongo.mongo import Mongo
from project.utilities.logger.logger_info import Logger



class Manager:
    def __init__(self,topic,kafka_config,uri_es,mong_setting):
        # Initialize all objects used in this service.

        self.folder_path=r"C:\Users\User\PycharmProjects\MuezzinProject07_09\project\data_files\podcasts"

        self.kafka=MyKafkaConsumer(topic,kafka_config)

        self.elastic=Elastic(uri_es)

        self.mongo=Mongo(mong_setting)

        self.processing=Process()


    def app(self):
        # Runs the service logic
        self.mongo.connect()

        self.kafka.open()

        self.elastic.init_es()

        self.processing.get_data_send_m_es(self.kafka, self.elastic, self.mongo, self.folder_path)


