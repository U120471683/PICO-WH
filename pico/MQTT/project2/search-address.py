import network
ssid = 'A590301'
password = 'A590301AA'

#ssid = 'shichan6'
#password = '038565301'#

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

while not wlan.isconnected():
    pass

print('network config:', wlan.ifconfig())
