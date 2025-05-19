from thingz import accelerometer
from thingz import sound
from thingz import led

def on_gesture_shake(gesture):
    sound.play_sample('rickroll')
    print('vous me devez tous 10 balles (non)')

def display_clear():
    print('[2J', end='')

def on_gesture_up(gesture):
    display_clear()
    print('')

accelerometer.on_gesture("shake", on_gesture_shake)
accelerometer.on_gesture("up", on_gesture_up)

print('Oriente la carte vers le haut.')
led.set_colors(255, 255, 255)

while True:
    pass
