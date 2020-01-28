from kafka import KafkaProducer
import json
import random
from time import sleep
from datetime import datetime

# Create an instance of the Kafka producer
producer = KafkaProducer(bootstrap_servers='10.30.80.164:29092',
                            value_serializer=lambda v: str(v).encode('utf-8'))

# Call the producer.send method with a producer-record
print("Ctrl+c to Stop")
i =0
while i <10:
    data = { 'tag ': 'blah',
        'name' : 'sam',
        'index' : i,
        'score': 
            {'row1': 100,
             'row2': 200
        }
    }   
    producer.send('kafka-python-topic', json.dumps(data))
    producer.send('oi eu sou o goku', random.randint(1, 999))
    i+=1