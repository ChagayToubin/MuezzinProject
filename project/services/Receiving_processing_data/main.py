from project.config.settings import Settings
from project.services.Receiving_processing_data.manager import Manager
from project.utilities.logger.logger_info import Logger
logger =Logger.get_logger()

def main():
    try:
        # Takes environment variables for the service
        kaf_config = Settings.configs_for_kafka_con
        uri_es = Settings.uri_es
        mongo_setting = Settings.mongo_setting
        folder_path=Settings.folder_path

        # Activates the service
        manager = Manager(["MetaData"], kaf_config, uri_es, mongo_setting,folder_path)
        manager.app()

        logger.info("Service activation was successful.")
    except Exception as e:
        logger.error(f"Retrieving file data failed because{e}")


if __name__ == '__main__':
    main()

    logger.info("servic Receiving_processing_data  end ")