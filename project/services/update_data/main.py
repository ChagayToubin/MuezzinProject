from project.services.update_data.manager import Manager
from project.config.settings import Settings

def main():

    uri_es=Settings.uri_es


    manager = Manager(uri_es)
    manager.app()

if __name__ == '__main__':
    main()

    print("finsih service 1")