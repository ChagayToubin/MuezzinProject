from project.config.settings import Settings
from project.services.Receiving_processing_data.manager import Manager
from project.utilities.logger.logger_info import Logger
logger =Logger.get_logger()

def main():
    # Takes environment variables for the service
    kaf_config = Settings.configs_for_kafka_con
    uri_es = Settings.uri_es
    mongo_setting = Settings.mongo_setting

    # Activates the service
    manager = Manager(["MetaData"], kaf_config, uri_es, mongo_setting)
    manager.app()


if __name__ == '__main__':
    main()

    logger.info("servic Receiving_processing_data  end ")