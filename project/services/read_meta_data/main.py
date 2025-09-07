
from project.config.settings import Settings
from project.services.read_meta_data.manager import Manager
def main():

    kaf_config=Settings.configs_for_kafka_pro

    path_file=r"C:\Users\User\PycharmProjects\MuezzinProject07_09\project\data_files\podcasts\download (1).wav"


    manager=Manager(kaf_config,path_file)
    manager.app()

if __name__ == '__main__':
    main()

    print("finsih service 1")
