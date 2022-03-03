import machine
import utime

led_external = machine.Pin(15,machine.Pin.OUT)
button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
    
        

value = 0 
while 1:
    if (button.value() == 1):
        value = value + 1
        print(value)
        led_external.value(1)
        utime.sleep(value)
    led_external.value(0)


