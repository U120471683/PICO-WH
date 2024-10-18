from machine import Pin, ADC, PWM
import time

# 定義輸入腳位
I_RED_PIN = 26  # A0
I_GREEN_PIN = 27  # A1
I_BLUE_PIN = 28  # A2

# 定義輸出腳位
O_RED_PIN = 2
O_GREEN_PIN = 3
O_BLUE_PIN = 5

# 初始化輸入腳位
r_adc = ADC(Pin(I_RED_PIN))
g_adc = ADC(Pin(I_GREEN_PIN))
b_adc = ADC(Pin(I_BLUE_PIN))

# 初始化輸出腳位
r_pwm = PWM(Pin(O_RED_PIN), freq=500)
g_pwm = PWM(Pin(O_GREEN_PIN), freq=500)
b_pwm = PWM(Pin(O_BLUE_PIN), freq=500)

def read_sensor():
    r = r_adc.read_u16()
    g = g_adc.read_u16()
    b = b_adc.read_u16()
    r_val = int(r / 65535 * 255)
    g_val = int(g / 65535 * 255)
    b_val = int(b / 65535 * 255)
    print(r_val, g_val, b_val)
    return r_val, g_val, b_val

def output_sensor(r, g, b):
    r_pwm.duty(r)
    g_pwm.duty(g)
    b_pwm.duty(b)

while True:
    r_val, g_val, b_val = read_sensor()
    output_sensor(r_val, g_val, b_val)
    time.sleep(0.1)