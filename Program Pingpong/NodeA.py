import paho.mqtt.client as mqtt
from time import sleep

mqttBroker = '34.101.187.83'
client = mqtt.Client('NodeB')
client.connect(mqttBroker)

def on_message(client, userdata, message):
    msg = message.payload.decode('utf-8')
    # client.publish('Topik_2', msg)
    print('Received: ' + msg)

while True:
    client.loop_start()
    client.subscribe('Topik_1')
    client.on_message = on_message
