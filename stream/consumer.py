from kafka import KafkaConsumer,KafkaProducer
from json import loads,dumps
import os
from joblib import load
import pandas as pd
import time
from build import PREDICTION_TOPIC,DELAY

model_path = os.path.abspath('../model/SARIMA.joblib')

consumer = KafkaConsumer('random_cpu_usage',
                         bootstrap_servers=['103.249.77.22:9092'],
                         auto_offset_reset='earliest',
                         enable_auto_commit=True,
                         group_id='ML',
                         value_deserializer=lambda x: loads(x.decode('utf-8')))

producer = KafkaProducer(bootstrap_servers=['103.249.77.22:9092'],
                         api_version=(0, 10, 1),
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

    
clf = load(model_path)

while True:
    # Message that came from producer
    m=consumer.poll(timeout_ms=50)
    if m is None:
        continue
    message=m.value
    Time=(pd.to_datetime(message['Time'],format='%Y-%m-%d %H:%M')).strftime("%Y-%m-%d %H:%M:%S")
    prediction=clf.predict(Time)[0]
    r={"Time":Time,"Original":message["Data"],"Prediction":prediction}
    producer.send(topic=PREDICTION_TOPIC,
                            value=r)
    producer.flush()
    time.sleep(DELAY)
    

consumer.close()