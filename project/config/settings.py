import os
import json

class Settings:
    # --------------------------------kafka----------------------------------
    kafka_host = os.getenv("KAFKA_HOST", "localhost")
    kafka_port = os.getenv("KAFKA_PORT", 9092)

    configs_for_kafka_pro = {
        'bootstrap_servers': f"{kafka_host}:{kafka_port}",
        'value_serializer' :lambda v: json.dumps(v).encode('utf-8')

    }
    configs_for_kafka_con={
        'bootstrap_servers': f"{kafka_host}:{kafka_port}",
        'group_id': "my-consumer",
        'auto_offset_reset': "earliest",
        'enable_auto_commit': 'True',
        'value_deserializer': lambda v: json.loads(v.decode("utf-8"))
    }

    # -------------------------------elastic--------------------
    # uri_es = os.getenv("URI", "http://localhost:9200")
    es_port=os.getenv("URI_PORT", None)
    es_host=os.getenv("URI_HOST", None)
    uri_es=[es_port,es_host]


    # ------------------------------mongo------------------------
    mongo_host = os.getenv("MONGO_HOST", "localhost")
    mongo_port=int(os.getenv("MONGO_PORT", 27017))
    mongo_db_name=os.getenv("MONGO_DB", "test_db")
    mongo_usr= os.getenv("MONGO_USER",None)
    mongo_password=os.getenv("MONGO_PASS",None)

    mongo_setting=[mongo_host,mongo_port,mongo_db_name,mongo_usr,mongo_password]

    # --------path to folder------------
    folder_path=r"C:\Users\User\PycharmProjects\MuezzinProject07_09\project\data_files\podcasts"

    #---------list words----------
    msg_bad = "R2Vub2NpZGUsV2FyIENyaW1lcyxBcGFydGhlaWQsTWFzc2FjcmUsTmFrYmEsRGlzcGxhY2VtZW50LEh1bWFuaXRhcmlhbiBDcmlzaXMsQmxvY2thZGUsT2NjdXBhdGlvbixSZWZ1Z2VlcyxJQ0MsQkRT"

    msg = "RnJlZWRvbSBGbG90aWxsYSxSZXNpc3RhbmNlLExpYmVyYXRpb24sRnJlZSBQYWxlc3RpbmUsR2F6YSxDZWFzZWZpcmUsUHJvdGVzdCxVTlJXQQ=="









