from board import A5, LED
from machine import Pin, PWM
from time import sleep

# p1 = Pin(A10, mode = Pin.OPEN_DRAIN)
# p1(0)
# P1(1)

LED = Pin(A5, mode = Pin.OPEN_DRAIN)
LED(0)
sleep(2)
LED(1)

# p1.freq(5e2)
# p1.duty(80)










