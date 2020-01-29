from kafka import KafkaProducer
import json
from time import sleep

producer = KafkaProducer(
    bootstrap_servers=['127.0.0.1:29092'],
    value_serializer=lambda x: json.dumps(x).encode('utf-8')                    
)

print("Ctrl+c to Stop")

i = 0

while i < 10:
    data = { 
        'tag ': 'blah',
        'name' : 'sam',
        'index' : i,
        'score': {
            'row1': 100,
            'row2': 200
        }
    }   

    producer.send('kafka-python-topic',value=texto)
    producer.flush()
    
    i += 1