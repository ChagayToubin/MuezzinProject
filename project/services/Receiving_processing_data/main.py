from project.config.settings import Settings
from project.services.Receiving_processing_data.manager import Manager


def main():
    # Takes environment variables for the service
    kaf_config = Settings.configs_for_kafka_con
    uri_es = Settings.uri_es
    mongo_setting = Settings.mongo_setting

    # Activates the service
    manager = Manager(["MetaData"], kaf_config, uri_es, mongo_setting)
    manager.app()


if __name__ == '__main__':
    main()

    print("finsih service 2")
