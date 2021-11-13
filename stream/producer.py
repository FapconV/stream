from kafka import KafkaProducer
from json import dumps
import time 
import random
import pandas as pd
from build import TRANSACTIONS_TOPIC,DELAY


def Rand(start, end, num):
    res = []
 
    for j in range(num):
        num = random.randint(start, end)
        res.append(num)  
    return res

producer = KafkaProducer(bootstrap_servers=['103.249.77.22:9092'],
                         api_version=(0, 10, 1),
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))
if producer is not None:

    time_series=pd.date_range('2022-12-07 16:00:00', periods = 100, freq ='H')
    data_r=Rand(0, 500, 100)
    for i in range(100):
      
      record = { "Time": ((pd.to_datetime(time_series[i],format='%Y-%m-%d %H:%M')).strftime("%Y-%m-%d %H:%M:%S")),"Data": data_r[i]}
     

      producer.send(topic=TRANSACTIONS_TOPIC,
                            value=record)
      producer.flush()
      time.sleep(DELAY)