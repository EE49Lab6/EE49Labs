from board import A5, LED
from machine import Pin, PWM
from time import sleep
import machine

LED = Pin(A5, mode = Pin.OPEN_DRAIN)

BRIGHTNESS = 0
p = PWM(LED, freq = 500, duty = 50)

def led_cb(timer):
	global BRIGHTNESS
	if BRIGHTNESS <= 100:
		p.duty(BRIGHTNESS)
	else:
		BRIGHTNESS = 0
	BRIGHTNESS += 1

t1 = machine.Timer(0)
t1.init(period = 50, mode=t1.PERIODIC, callback=led_cb)


# sleep(2)
# p.duty(100)




# p1.freq(5e2)
# p1.duty(80)










