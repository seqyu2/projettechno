from thingz import accelerometer
from thingz import led
from thingz import sound

def display_clear():
    print('[2J', end='')

def on_gesture_up(gesture):
    display_clear()
    print('')
    // TODO: le jeu en lui même, faut arrêter de faire le con avec les easter eggs

def on_gesture_shake(gesture):
    sound.play_sample('rickroll')
    print('vous me devez tous 10 balles (non)')

accelerometer.on_gesture("up", on_gesture_up)
accelerometer.on_gesture("shake", on_gesture_shake)

print('Oriente la carte vers le haut.')
led.set_colors(255, 255, 255)

while True:
    pass
