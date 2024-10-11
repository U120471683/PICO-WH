import network

ssid = '你的Wi-Fi名稱'
password = '你的Wi-Fi密碼'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

while not wlan.isconnected():
    pass

print('network config:', wlan.ifconfig())
