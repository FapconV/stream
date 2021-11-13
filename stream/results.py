from kafka import KafkaConsumer

from json import loads

consumer = KafkaConsumer(
    'Random_CPU_Usage_Predictions',
     bootstrap_servers=['103.249.77.22:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='mlai',
     value_deserializer=lambda x: loads(x.decode('utf-8')))



PREDICTIONS=[]
while True:
    message=consumer.poll(timeout_ms=50)
    if message is None:
        continue
    print(message.value)
    PREDICTIONS.append(message.value)

consumer.close()