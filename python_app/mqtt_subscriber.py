import json
import paho.mqtt.client as mqtt
from db_handlers.mongo_handler import store_temperature
from db_handlers.sql_handler import store_temperature_sql
from db_handlers.neo4j_handler import store_device_graph

broker = "localhost"
port = 1883
topics = [("sensor/temperature", 0), ("network/device", 0)]

def on_connect(client, userdata, flags, rc):
    print("Connected with result code", rc)
    client.subscribe(topics)

def on_message(client, userdata, msg):
    payload = json.loads(msg.payload.decode())
    print(f"Received from {msg.topic}: {payload}")
    
    if msg.topic == "sensor/temperature":
        store_temperature(payload)
        store_temperature_sql(payload["temperature"])
    elif msg.topic == "network/device":
        store_device_graph(payload["device_id"], payload["network_id"])

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, port)
client.loop_forever()
