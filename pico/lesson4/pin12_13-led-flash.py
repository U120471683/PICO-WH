from machine import Timer, Pin

import time

#tim = Timer(period=5000, mode=Timer.ONE_SHOT, callback=lambda t:print(1))
#tim.init(period=1000, mode=Timer.PERIODIC, callback=lambda t:print(2))
green_led = Pin(13,Pin.OUT)
green_count = 0
def green_led_mycallback(t:Timer):
    global green_count
    green_count += 1
    #print(f"目前mycallback被執行:{count}次")
    green_led.toggle()
    print("green_led初執行")
    if green_count >= 200:
        t.deinit()

green_led_timer = Timer(period=1000,mode=Timer.PERIODIC,callback=green_led_mycallback)

red_led = Pin(12,Pin.OUT)
red_count = 0
def red_led_mycallback(t:Timer):
    global red_count
    red_count = red_count + 1
    #print(f"目前mycallback被執行:{count}次")
    
    red_led.toggle()
    print("red_led初執行")
    if red_count >= 100:
        t.deinit()
red_led_timer = Timer(period=2000,mode=Timer.PERIODIC,callback=red_led_mycallback)        
        
led = Pin(15, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_DOWN)

while True:
    if button.value():
        led.toggle()
        time.sleep(0.5)   
        

