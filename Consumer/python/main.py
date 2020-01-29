from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'kafka-python-topic',
    bootstrap_servers=['127.0.0.1:29092'],
    auto_offset_reset='latest',
    enable_auto_commit=True,
    value_deserializer=lambda x: loads(x.decode('utf-8'))
)

for message in consumer:
    message = message.value
    print(message)