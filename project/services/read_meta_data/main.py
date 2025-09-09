
from project.config.settings import Settings
from project.services.read_meta_data.manager import Manager
from project.utilities.logger.logger_info import Logger
def main():


    kaf_config=Settings.configs_for_kafka_pro

    path_folder=r"C:\Users\User\PycharmProjects\MuezzinProject07_09\project\data_files\podcasts"


    manager=Manager(kaf_config,path_folder)
    manager.app()

if __name__ == '__main__':
    main()

    print("finsih service 1")


