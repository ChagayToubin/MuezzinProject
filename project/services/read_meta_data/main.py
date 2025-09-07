from project.config.settings import Settings
from project.services.read_meta_data.manager import Manager
def main():

    KAFKA_URI=Settings.KAFKA_URI
    path_file=r"C:\Users\User\PycharmProjects\MuezzinProject07_09\project\data_files\podcasts\download (4).wav"
    manager=Manager(KAFKA_URI,path_file)
    manager.app()


if __name__ == '__main__':
    main()
    print("--")