from board import A5, A21, LED
from machine import Pin, PWM
from time import sleep
import machine

p1 = pwm(A5, freq = 5000, duty = 20, timer = 0)

p2 = PWM(A, freq = 8000, duty = 60, timer = 1)