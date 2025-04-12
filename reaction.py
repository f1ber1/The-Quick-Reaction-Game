from gpiozero import LED,Button
from time import sleep,monotonic
from random import uniform
from signal import pause

led = LED(4)
right_button = Button(15)
left_button = Button(14)

left_name = input('left player name:')
right_name = input('left player name:')
game_active = False
start_time = 0
timeout = 5
best_times = {left_name:None,right_name:None}

def pressed(button):
	global game_active
	if game_active:
		reaction_time = monotonic() - start_time
		reaction_ms = int(reaction_time *1000)
		winner = left_name if button.pin.number == 14 else right_name
		if not best_times[winner] or reaction_ms < best_times[winner]:best_times[winner] = reaction_ms
		print(f'\n{winner} won the game!Reaction time is {reaction_ms}ms')
		game_active = False

left_button.when_pressed = pressed
right_button.when_pressed = pressed

try:
	while True:
		print('new round will start in 3 secouds!')
		sleep(3)

		game_active = False
		led.on()
		sleep(uniform(5,10))
		led.off()
		game_active = True
		start_time = monotonic()
		while monotonic() - start_time < timeout and game_active:
			sleep(0.01)
except KeyboardInterrupt:
	led.close()
	print('\n game quit')
	print('best time:')
	for player,time in best_times.items():
		print(f'{player}:{time}ms' if time else f'{player}:no record')
