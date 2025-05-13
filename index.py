from thingz import led

def display_clear():
    print('[2J', end='')

display_clear()

while True:
    if False:
        pass
    else:
        led.set_blue(255)
