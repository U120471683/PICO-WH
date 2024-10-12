import time
import binascii
import machine
from umqtt.simple import MQTTClient
from machine import Pin
import tools

def main():
    #try:
        tools.connect()
        mqtt = MQTTClient(CLIENT_ID, SERVER,user='pi',password='raspberry')
        
        print('debug')
          
        print(mqtt.connect())
        print('debug')
        while True:   
            mqtt.publish('SA-59/LIGHT_LEVEL', b"34.516")
            time.sleep_ms(2000)
    #except Exception:
        #mqtt.disconnect()
    
if __name__ == '__main__':
    # Default MQTT server to connect to
    SERVER = "192.168.0.252"
    CLIENT_ID = binascii.hexlify(machine.unique_id())
    TOPIC = b"SA-59/chickenHouse/溫度"
    main()