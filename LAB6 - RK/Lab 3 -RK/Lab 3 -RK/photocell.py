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

while True:
	v = ina.voltage()
	i = ina.current()
	p = ina.power()
	if i!=0:
		r = v/i
	else:
		r = 0
	print("V = {:6.2f}, I = {:6.2f}, P = {:6.2f})".format(v, i, p))
	time.sleep(1)

''' Insert your code here to read and print voltage, current, and power from ina219. '''