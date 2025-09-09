from pathlib import Path

from project.config.settings import Settings
from project.services.read_meta_data.manager import Manager
from project.utilities.logger.logger_info import Logger
base_dir = Path(__file__).resolve().parent


def main():
    # print(base_dir)
    # print("----")
    # print(r"C:\Users\User\PycharmProjects\MuezzinProject07_09\project\data_files\podcasts")
    # print("----")
    # path_folder=rf"{base_dir}project\data_files\podcasts"

    # Takes environment variables for the service
    kaf_config = Settings.configs_for_kafka_pro

    path_folder = r"C:\Users\User\PycharmProjects\MuezzinProject07_09\project\data_files\podcasts"

    # Activates the service
    manager = Manager(kaf_config, path_folder, "MetaData")
    manager.app()


if __name__ == '__main__':
    main()

    print("finsih service 1")
