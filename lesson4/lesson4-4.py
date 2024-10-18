from machine import Timer

# 創建一個一次性定時器，5秒後執行回調函數 /
#Timer.ONE_SHOT 模式表示定時器只會觸發一次。
#Timer.PERIODIC 模式表示定時器會週期性觸發。
#callback 是定時器觸發時執行的回調函數。是定時器觸發時執行的函數
tim = Timer(period=5000, mode=Timer.ONE_SHOT, callback=lambda t:print(1))

# 重新初始化定時器為週期性定時器，每秒執行一次回調函數

tim.init(period=1000, mode=Timer.PERIODIC, callback=lambda t:print(2))

#定時器首先被設定為一次性定時器，5秒後觸發並打印數字1。接著，定時器被重新初始化為週期性定時器
#，每秒觸發一次並打印數字2。
