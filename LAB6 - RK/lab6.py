from board import LED, A9, ADC0, A5, A21
from machine import Pin, ADC, PWM, 
from micropython import schedule
import time
import machine


# define frequency for each tone
C3 = 131
CS3 = 139
D3 = 147
DS3 = 156
E3 = 165
F3 = 175
FS3 = 185
G3 = 196
GS3 = 208
A3 = 220
AS3 = 233
B3 = 247
C4 = 262
CS4 = 277
D4 = 294
DS4 = 311
E4 = 330
F4 = 349
FS4 = 370
G4 = 392
GS4 = 415
A4 = 440
AS4 = 466
B4 = 494
C5 = 523
CS5 = 554
D5 = 587
DS5 = 622
E5 = 659
F5 = 698
FS5 = 740
G5 = 784
GS5 = 831
A5_ = 880
AS5 = 932
B5 = 988
C6 = 1047
CS6 = 1109
D6 = 1175
DS6 = 1245
E6 = 1319
F6 = 1397
FS6 = 1480
G6 = 1568
GS6 = 1661
A6 = 1760
AS6 = 1865
B6 = 1976
C7 = 2093
CS7 = 2217
D7 = 2349
DS7 = 2489
E7 = 2637
F7 = 2794
FS7 = 2960
G7 = 3136
GS7 = 3322
A7 = 3520
AS7 = 3729
B7 = 3951
C8 = 4186
CS8 = 4435
D8 = 4699
DS8 = 4978
# Bach Prelude in C.

bach = [
C4, E4, G4, C5, E5, G4, C5, E5, C4, E4, G4, C5, E5, G4, C5, E5,
C4, D4, G4, D5, F5, G4, D5, F5, C4, D4, G4, D5, F5, G4, D5, F5,
B3, D4, G4, D5, F5, G4, D5, F5, B3, D4, G4, D5, F5, G4, D5, F5,
C4, E4, G4, C5, E5, G4, C5, E5, C4, E4, G4, C5, E5, G4, C5, E5,
C4, E4, A4, E5, A5_, A4, E5, A4, C4, E4, A4, E5, A5_, A4, E5, A4,
C4, D4, FS4, A4, D5, FS4, A4, D5, C4, D4, FS4, A4, D5, FS4, A4, D5,
B3, D4, G4, D5, G5, G4, D5, G5, B3, D4, G4, D5, G5, G4, D5, G5,
B3, C4, E4, G4, C5, E4, G4, C5, B3, C4, E4, G4, C5, E4, G4, C5,
B3, C4, E4, G4, C5, E4, G4, C5, B3, C4, E4, G4, C5, E4, G4, C5,
A3, C4, E4, G4, C5, E4, G4, C5, A3, C4, E4, G4, C5, E4, G4, C5,
D3, A3, D4, FS4, C5, D4, FS4, C5, D3, A3, D4, FS4, C5, D4, FS4, C5,
G3, B3, D4, G4, B4, D4, G4, B4, G3, B3, D4, G4, B4, D4, G4, B4
]

P1 = Pin(A5, mode = Pin.OPEN_DRAIN)
P2 = Pin(A21, mode = Pin.OPEN_DRAIN)

# BRIGHTNESS = 0
p2 = PWM(P2, freq = 500, duty = 50, timer = 1)
p1 = PWM(P1, freq = 1, duty = 50, timer = 0)
# def led_cb(timer):
# 	global BRIGHTNESS
# 	if BRIGHTNESS <= 100:
# 		p.duty(BRIGHTNESS)
# 	else:
# 		BRIGHTNESS = 0
# 	BRIGHTNESS += 1

# t1 = machine.Timer(0)
# t1.init(period = 50, mode=t1.PERIODIC, callback=led_cb)

NOTE = 0
def tune_cb(timer):
	global NOTE
	if NOTE <= len(bach):
		p1.freq(bach[NOTE])
	else:
		NOTE = 0
	NOTE += 1

BRIGHTNESS = 0
def led_cb(timer):
	global BRIGHTNESS
	if BRIGHTNESS <= 100:
		p2.duty(BRIGHTNESS)
	else:
		BRIGHTNESS = 0
	BRIGHTNESS += 1

t2 = machine.Timer(1)
t2.init(period = 50, mode=t2.PERIODIC, callback=led_cb)

t1 = machine.Timer(0)
t1.init(period = 500, mode=t1.PERIODIC, callback=tune_cb)


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
		
	else:
		led(0)
	last_state = state


button.irq(button_irq_handler, trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING)

