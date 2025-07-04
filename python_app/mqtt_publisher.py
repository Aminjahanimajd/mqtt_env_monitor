import time
import json
import random
import paho.mqtt.client as mqtt

broker = "localhost"
port = 1883

client = mqtt.Client()
client.connect(broker, port)

while True:
    # Existing: publish temperature
    temp = round(random.uniform(18.0, 30.0), 2)
    payload = {"temperature": temp}
    client.publish("sensor/temperature", json.dumps(payload))
    print("Published to temperature topic:", payload)

    # New: publish device-network data
    device_id = f"sensor_{random.randint(1, 5)}"
    network_id = "env_net_1"
    payload = {"device_id": device_id, "network_id": network_id}
    client.publish("network/device", json.dumps(payload))
    print("Published to network topic:", payload)

    time.sleep(3)  # wait 3 seconds between messages
