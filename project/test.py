from kafka import KafkaProducer, KafkaConsumer
import json

# Producer example
producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))
producer.send('my_topic', {'key': 'value'})
producer.flush()

# Consumer example
consumer = KafkaConsumer('my_topic',
                         bootstrap_servers='localhost:9092',
                         auto_offset_reset='earliest',
                         enable_auto_commit=True,
                         group_id='my-group',
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')))

for message in consumer:
    print(f"Received message: {message.value}")


