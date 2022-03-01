import paho.mqtt.client as mqtt
import time, random, threading
import multiprocessing as mp

# client, user and device details
serverUrl   = "34.101.187.83"
clientId    = "NodeA"

# task queue to overcome issue with paho when using multiple threads:
task_queue = mp.Queue()

# display all incoming messages
def on_message(client, userdata, message):
    payload = message.payload.decode("utf-8")
    print(" < republish message " + payload)
#     publish("Topik_2", payload)
 

# # send temperature measurement
# def send_data():
#     temperature = random.randint(10, 20)
#     print(" > Sending temperature " +str(temperature))
#     publish("Topik_1", temperature)

# # publish a message
# def publish(topic, message):
#     client.publish(topic, message)
    

# # main device loop
# def device_loop():
#     while True:
#         task_queue.put(send_data)
#         time.sleep(2)

# connect the client to Cumulocity IoT and register a device
client = mqtt.Client(clientId)
client.on_message = on_message

client.connect(serverUrl)
client.loop_start()

client.subscribe("Topik_1")

# device_loop_thread = threading.Thread(target = device_loop)
# device_loop_thread.daemon = True
# device_loop_thread.start()

# process all tasks on queue
try:
    while True:
        task = task_queue.get()
        task()
except (KeyboardInterrupt, SystemExit):
    print("Received keyboard interrupt, quitting ...")
    exit(0)