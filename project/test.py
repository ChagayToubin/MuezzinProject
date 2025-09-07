# from kafka import KafkaProducer, KafkaConsumer
# import json
#
# # Producer example
# producer = KafkaProducer(bootstrap_servers='localhost:9092',
#                          value_serializer=lambda v: json.dumps(v).encode('utf-8'))
# producer.send('my_topic', {'key': 'value'})
# producer.flush()
#
# # Consumer example
# consumer = KafkaConsumer('my_topic',
#                          bootstrap_servers='localhost:9092',
#                          auto_offset_reset='earliest',
#                          enable_auto_commit=True,
#                          group_id='my-group',
#                          value_deserializer=lambda x: json.loads(x.decode('utf-8')))
#
# for message in consumer:
#     print(f"Received message: {message.value}")
#
#
from pathlib import Path
path=r"C:\Users\User\PycharmProjects\MuezzinProject07_09\project\data_files\podcasts"
folder_path = Path(r"C:\Users\User\PycharmProjects\MuezzinProject07_09\project\data_files\podcasts")  # Replace with the actual path to your folder

all_files = list(folder_path.glob("*"))  # Get all files and directories in the folder
files_only = [f for f in all_files if f.is_file()] # Filter out directories
for file in files_only:
    file_path = Path(f"{path}+{file.name}")
    print(str(file_path))
    print(file.name)

    # stats = file_path.stat()
    # file_name = file_path.name
    # size = stats.st_size