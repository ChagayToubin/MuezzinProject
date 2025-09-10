from pathlib import Path

from project.config.settings import Settings
from project.services.read_meta_data.manager import Manager
from project.utilities.logger.logger_info import Logger

logger =Logger.get_logger()
base_dir = Path(__file__).resolve().parent.parent.parent
print(base_dir)
import os

def main():



    # Takes environment variables for the service
    kaf_config = Settings.configs_for_kafka_pro

    print(rf"{base_dir}")

    print("----")
    path_folder = r"C:\Users\User\PycharmProjects\MuezzinProject07_09\project\data_files\podcasts"
    print((type(path_folder),path_folder))
    # Activates the service

    manager = Manager(kaf_config, path_folder, "MetaData")
    manager.app()


if __name__ == '__main__':
    main()

    logger.info("servic read_meta_data end ")