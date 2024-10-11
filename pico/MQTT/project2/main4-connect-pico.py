import network
import time

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('shichan6','038565301')

while not wlan.isconnected() and wlan.status() >= 0:
    print("Waiting to connect:")
    time.sleep(1)
    
print(f"Connect to" ,{wlan.ifconfig()})
