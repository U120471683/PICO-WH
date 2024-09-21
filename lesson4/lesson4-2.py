from machine import Pin
import time
led = Pin("LED", mode=Pin.OUT)
while True:
    led.on()
    print('hello')
    time.sleep(5)
    led.off()
    time.sleep(5)