# Blinking program 
# incoporate/include modules
import machine #module with all the microcontroller stuff
import time #module with time methods

# Make the led object 
# Green led is GPIO PIn 0
led = machine.Pin(0, machine.Pin.OUT)
# Infinite loop
while True: 
  led.value(1) # turn on the LED
  time.sleep(0.2)
  led.value(0)
  time.sleep(0.2)
