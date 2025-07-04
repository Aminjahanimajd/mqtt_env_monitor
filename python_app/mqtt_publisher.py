import time
import random
import paho.mqtt.client as mqtt

broker = "localhost"
port = 1883
topic = "sensor/temperature"

client = mqtt.Client()
client.connect(broker, port)

while True:
    temp = round(random.uniform(18.0, 30.0), 2)
    payload = f'{{"temperature": {temp}}}'
    client.publish(topic, payload)
    print(f"Published: {payload}")
    time.sleep(3)
