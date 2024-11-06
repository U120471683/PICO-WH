#! usr/bin/micropython

'''
led->gpio15
光敏電阻 -> gpio28
可變電阻 -> gpio26
內建溫度sensor -> adc最後1pin,共5pin
'''

from machine import Timer,ADC,Pin,PWM,RTC
import binascii
from umqtt.simple import MQTTClient
import tools,config


def do_thing(t):
    '''
    :param t:Timer的實體
    負責偵測溫度和光線
    每2秒執行1次
    '''
    conversion_factor = 3.3 / (65535)
    reading = adc.read_u16() * conversion_factor
    #temperature = 27 - (reading - 0.706)/0.001721  
    temperature = round(27 - (reading - 0.706)/0.001721,2)  
    print(f'溫度:{temperature}')
    mqtt.publish('SA-59/TEMPERATURE', f'{temperature}')
    blynk_mqtt.publish('ds/temperature', f'{temperature}')
    
    adc_value = adc_light.read_u16() #光線的值
    print(f'光線:{adc_value}')
    line_state = 0 if adc_value < 20000 else 1 #line_state = 0(adc_value < 20000) :關燈
                                                        #line_state = 1(adc_value >= 20000) : 開燈
    print(f'光線:{line_state}')
    mqtt.publish('SA-59/LINE_LEVEL', f'{line_state}')
    blynk_mqtt.publish('ds/line_status', f'{line_state}')
    
    
    
def do_thing1(t):
    '''
    :param t:Timer的實體
    負責可變電阻和改變led的亮度
    '''    
    
    duty = adc1.read_u16()
    pwm.duty_u16(duty)
    light_level = round(duty/65535*10)
    print(f'可變電阻:{light_level}')
    mqtt.publish('SA-59/LED_LEVEL', f'{light_level}')
    blynk_mqtt.publish('ds/led_level', f'{light_level}')
    

def main():
    #pass
    global blynk_mqtt 
    print(config.BLYNK_MQTT_BROKER)
    print(config.BLYNK_TEMPLATE_ID)
    blynk_mqtt = MQTTClient(config.BLYNK_TEMPLATE_ID, config.BLYNK_MQTT_BROKER,user='device',password='eVDqgsEJxLNNOkVv1cLT5FampGzj9fbQ',keepalive=60)
    blynk_mqtt.connect()   

if __name__ == '__main__':
    adc = ADC(4) #內建溫度
    adc1 = ADC(Pin(26)) #可變電阻
    adc_light = ADC(Pin(28)) #光敏電阻
    pwm = PWM(Pin(15),freq=50) #pwm led
    #連線internet
    try:
        tools.connect()
    except RuntimeError as e:
        print(e)
    except Exception:
        print('不知名的錯誤')
    else:
        #MQTT
        SERVER = "192.168.1.125"  #SERVER=shichan@shichan3
        #SERVER = "192.168.1.128"  #SERVER=shichan@shichan4
        #SERVER = "192.168.0.104"  #SERVER=shichan@shichan4致理
        #SERVER = "192.168.0.252"
        CLIENT_ID = binascii.hexlify(machine.unique_id())
        mqtt = MQTTClient(CLIENT_ID, SERVER,user='pi',password='raspberry')
        mqtt.connect()
        t1 = Timer(period=2000, mode=Timer.PERIODIC, callback=do_thing)
        t2 = Timer(period=2000, mode=Timer.PERIODIC, callback=do_thing1)   
    blynk_mqtt=None
    main()