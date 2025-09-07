import os
import json

class Settings:

    kafka_host = os.getenv("KAFKA_HOST", "localhost")
    kafka_port = os.getenv("KAFKA_PORT", 9092)

    configs_for_kafka_client = {
        'bootstrap_servers': f"{kafka_host}:{kafka_port}",
        'value_serializer' :lambda v: json.dumps(v).encode('utf-8')

    }


