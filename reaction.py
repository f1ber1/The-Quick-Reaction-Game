from gpiozero import LED,Button
from time import sleep
from random import uniform
from signal import pause

led = LED(4)
right_button = Button(15)
left_button = Button(14)


left_name = input('left player name is:')
right_name = input('right player name is:')

game_active = False

def pressed(button):
	global game_active
	if game_active:
		winner = left_name if button.pin.number == 14 else right_name
		print(f"\n{winner} won the game!")
		game_active = False
right_button.when_pressed = pressed
left_button.when_pressed = pressed

try:
	while True:
		game_active = False
		print("New round")
		led.on()
		delay = uniform(5,10)
		sleep(delay)
		led.off()
		game_active = True
		timeout = 5
		while timeout > 0 and game_active:
			sleep(0.1)
			timeout -=0.1
except KeyboardInterrupt:
	led.close()
	print("game over")


