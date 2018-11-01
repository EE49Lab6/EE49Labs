from mqttclient import MQTTClient
import network
import sys
import time
"""
Publish and subscribe hello statements to test MQTT on ESP32
Go to https://hobbyquaker.github.io/mqtt-admin/ to interact with your microcontroller via MQTT
Go to https://iot.eclipse.org/getting-started/ for socket parameters.
Topic must match between microcontroller and web client.
"""

# Important: change the line below to a unique string,
# e.g. your name/esp34/helloworld
session = "peanutbutter/esp34/helloworld"
BROKER = "iot.eclipse.org"

# check wifi connection
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
ip = wlan.ifconfig()[0]
if ip == "0.0.0.0":
	print("no wifi connection")
	sys.exit()
else:
	print("connected to WiFi at IP", ip)

# connect to MQTT broker
print("Connecting to MQTT broker", BROKER, "...", end="")
mqtt = MQTTClient(BROKER)
print("Connected!")

# Define function to execute when a message is recieved on a subscribed topic.
def mqtt_callback(topic, msg):
	print("RECEIVE topic = {}, msg = {}".format(topic.decode(utf-8),msg.decode(utf-8)))

# Set callback function
mqtt.set_callback(mqtt_callback)

# Set a topic you will subscribe too. Publish to this topic via web client and watch microcontroller recieve messages.
mqtt.subscribe(session + "/host/hello")

for t in range(100):
# Microcontroller sends hellos statements.
	topic = "{}/mcu/hello".format(session)
	data = "hello" + str(t)
	print("send topic='{}' data='{}'".format(topic, data))
	mqtt.publish(topic, data)
	# Check for any messages in subscribed topics.
	for _ in range(10):
		mqtt.check_msg()
		time.sleep(0.5)
# free up resources
# alternatively reset the microphyton board before executing this program again
mqtt.disconnect()