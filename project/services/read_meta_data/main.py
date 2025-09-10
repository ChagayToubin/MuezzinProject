from project.config.settings import Settings
from project.services.read_meta_data.manager import Manager
from project.utilities.logger.logger_info import Logger

logger = Logger.get_logger()


def main():
    # Takes environment variables for the service
    kaf_config = Settings.configs_for_kafka_pro

    path_folder = Settings.folder_path
    try:

        # Activates the service

        manager = Manager(kaf_config, path_folder, "MetaData")
        manager.app()
        logger.info("Service activation was successful.")

    except Exception as e:
        logger.error(f"Retrieving file data failed because{e}")


if __name__ == '__main__':
    main()

    logger.info("servic read_meta_data end ")
