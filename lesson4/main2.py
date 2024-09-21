#指定DELAY的次數
from machine import Timer

#tim = Timer(period=5000, mode=Timer.ONE_SHOT, callback=lambda t:print(1))
#tim.init(period=1000, mode=Timer.PERIODIC, callback=lambda t:print(2))
count = 0

def mycallback(t:Timer):  #將led_timer傳給t
    global count #此變數為全域變數
    count = count + 1
    print(f"目前mycallback被執行:{count}次")
    if count >= 10:
        t.deinit()

led_timer = Timer(period=1000,mode=Timer.PERIODIC,callback=mycallback)