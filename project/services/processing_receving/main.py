from project.config.settings import Settings
from project.services.processing_receving.manager import Manager


def main():
    kaf_config = Settings.configs_for_kafka_con

    uri_es = Settings.uri_es

    manager = Manager(["MetaData"], kaf_config, uri_es)

    manager.app()

if __name__ == '__main__':
    main()

    print("finsih service 2")
