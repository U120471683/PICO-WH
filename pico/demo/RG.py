from machine import Pin
import utime

# 定義紅、綠、藍 LED 的腳位
led_r = Pin(2, Pin.OUT)
led_g = Pin(3, Pin.OUT)
led_b = Pin(5, Pin.OUT)

# 設定共陽極 RGB LED 的初始狀態為關閉
led_r.value(1)
led_g.value(1)
led_b.value(1)

while True:
    # 紅色 LED 閃爍
    led_r.toggle()
    utime.sleep(1)
    led_r.toggle()

    # 綠色 LED 閃爍
    #led_g.toggle()
    #utime.sleep(1)
    #led_g.toggle()
    #utime.sleep(1)

    # 藍色 LED 閃爍
    led_b.toggle()
    utime.sleep(1)
    led_b.toggle()
    utime.sleep(1)