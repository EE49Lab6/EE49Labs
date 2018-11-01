from board import LED
from machine import Pin
from time import sleep

led = Pin(LED, mode=Pin.OUT)

while True:
	led (1)
	sleep (1)
	led (0)
	sleep (1)
