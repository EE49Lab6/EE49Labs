from mqttclient import MQTTClient
from math import sin
import network
import sys
"""
Send measurement results from microphyton board to host computer.
Use in combination with mqtt_plot_host.py.

print
 statements throughout the code are for testing and can be removed once
verification is complete.
"""

# Important: change the line below to a unique string,
# e.g. your name & make corresponding change in mqtt_plot_host.py
session = "peanutbutter/esp34/helloworld"
BROKER = "iot.eclipse.org"

# check wifi connection
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
ip = wlan.ifconfig()[0]
if ip == '0.0.0.0':
	print("no wifi connection")
	sys.exit()
else:
	print("connected to WiFi at IP", ip)

# connect to MQTT broker
print("Connecting to MQTT broker", BROKER, "...", end="")
mqtt = MQTTClient(BROKER)
print("Connected!")

# send data
# In this sample, we send "fake" data. Replace this code to send useful data,
# e.g. measurement results.
from ina219 import INA219
from machine import I2C, Pin
from board import SDA, SCL
import time

i2c = I2C(id=0, scl=Pin(SCL), sda=Pin(SDA), freq=100000)

print("scanning I2C bus ...")
print("I2C:", i2c.scan())

SHUNT_RESISTOR_OHMS = 0.1
ina = INA219(SHUNT_RESISTOR_OHMS, i2c)
ina.configure()

ResistanceCheck = True

R = [0]
P = [0]
while ResistanceCheck:
	v = ina.voltage()
	i = ina.current()
	p = ina.power()
	r = 0
	if i!=0:
		r = v/i
	else:
		r = 0
	if r > .8:
		ResistanceCheck = False
		print("Resistance is greater than 800ohms")
	print("V = {:6.2f}, R = {:6.2f}, P = {:6.2f})".format(v, r, p))
	if p > 1.1*P[-1] or p < 0.9*P[-1]:
		R.append(r)
		P.append(p)
		data = "{},{}".format(r,p)
		topic = "{}/data".format(session)
		mqtt.publish(topic, data)
		print("publishing data")
	time.sleep(0.3)


# do the plotting (on host)
print("tell host to do the plotting ...")
mqtt.publish("{}/plot".format(session), "create the plot")

# free up resources
# alternatively reset the microphyton board before executing this program again
mqtt.disconnect()