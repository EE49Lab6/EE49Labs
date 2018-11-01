from board import LED, A9, ADC0, A5, A21
from machine import Pin, ADC, PWM, 
from micropython import schedule
import time
import machine

button = Pin(A9, mode=Pin.IN, pull=Pin.PULL_UP)

led = Pin(LED, mode=Pin.OUT)

count 		= 0
last_state 	= 0
last_time 	= time.ticks_ms()

def report(pin):
	global count
	if pin() == 0:
		print("> pressed {} times".format(count))
	else:
		print("Button pressed {} times".format(count))

def button_irq_handler(button):
	global count, last_time, last_state, delta_t, state, t
	state 	= button()
	t 		= time.ticks_ms()
	delta_t = t - last_time
	if delta_t > 20 and state==1 and last_state ==0:
		last_time = t
		count +=1
		schedule(report, button)
		led(1)
	else:
		led(0)
	last_state = state


button.irq(button_irq_handler, trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING)


    


# while True:
# 	if button():
# 		led(1)
# 		count = count + 1
# 	else:
# 		led(0)
# print(count)

