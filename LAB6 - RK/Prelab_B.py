from board import DAC2, ADC4
from machine import Pin, DAC, ADC
import time

dac2 = DAC(Pin(DAC2))
adc4 = ADC(Pin(ADC4))
adc4.atten(ADC.ATTN_11DB)

for x in range(1,255):
	dac2.write(x)
	print(x)
	time.sleep(.1)
	U = adc4.read()
	print(U)

# # set full-scale range


# # perform conversion



# time.sleep(1)


# # perform conversion
# code2 = dac2.write(code)
# print(code2)
