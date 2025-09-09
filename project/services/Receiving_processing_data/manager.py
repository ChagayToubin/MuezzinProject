
from project.services.Receiving_processing_data.data_processing import Process
from project.utilities.kafka.kafka_consumer.kafka_sub import MyKafkaConsumer
from project.utilities.elastic.elastic import Elastic
from project.utilities.mongo.mongo import Mongo
from project.utilities.logger.logger_info import Logger


logger=Logger.get_logger()
class Manager:
    def __init__(self,topic,kafka_config,uri_es,mong_setting):
        # Initialize all objects used in this service.

        try:

            self.folder_path=r"C:\Users\User\PycharmProjects\MuezzinProject07_09\project\data_files\podcasts"

            self.kafka=MyKafkaConsumer(topic,kafka_config)


            self.elastic=Elastic(uri_es)

            self.mongo=Mongo(mong_setting)

            self.processing=Process()

            logger.info("Initialization of objects was success")

        except Exception as e:
            logger.error(f"Initialization of objects failed.{e}")




    def app(self):
        # Runs the service logic
        try:
            self.mongo.connect()

            self.kafka.open()

            self.elastic.init_es()
            logger.info("Initialization of objects was success")
        except Exception as e:
            logger.error(f"Initialization of objects failed becuas.{e}")

        self.processing.get_data_send_m_es(self.kafka, self.elastic, self.mongo, self.folder_path)



