import os
import json

class Settings:

    kafka_host = os.getenv("KAFKA_HOST", "localhost")
    kafka_port = os.getenv("KAFKA_PORT", 9092)

    configs_for_kafka_pro = {
        'bootstrap_servers': f"{kafka_host}:{kafka_port}",
        'value_serializer' :lambda v: json.dumps(v).encode('utf-8')

    }
    configs_for_kafka_con={
        'bootstrap_servers': f"localhost:9092",
        'group_id': "my-consumer",
        'auto_offset_reset': "earliest",
        'enable_auto_commit': 'True',
        'value_deserializer': lambda v: json.loads(v.decode("utf-8"))
    }
    uri_es = os.getenv("URI", "http://localhost:9200")





