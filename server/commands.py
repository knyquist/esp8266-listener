import machine


def led_on():
    print('Performing action: turn LED 2 on')
    pin = machine.Pin(2, machine.Pin.OUT)
    pin.value(0)

def led_off():
    print('Performing action: turn LED 2 off')
    pin = machine.Pin(2, machine.Pin.OUT)
    pin.value(1)