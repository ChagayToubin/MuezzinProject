from project.services.update_data.manager import Manager
from project.config.settings import Settings
from project.utilities.logger.logger_info import Logger

logger = Logger.get_logger()


def main():
    # This service deals with updating data on Elastic.
    try:

        uri_es = Settings.uri_es

        manager = Manager(uri_es)
        manager.app()
        logger.info("Data update completed successfully.")

    except Exception as e:
        logger.error(f"Data update failed because{e}")


if __name__ == '__main__':
    main()

    print("finsih service 1")
