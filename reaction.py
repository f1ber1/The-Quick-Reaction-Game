from gpiozero import LED,Button
from time import sleep
from random import uniform

led = LED(4)
right_button = Button(15)
left_button = Button(14)

def pressed(button):
	print(str(button.pin.number) + 'won the game')

led.on()
sleep(uniform(5,10))
led.off()

right_button.when_pressed=pressed
left_button.when_pressed=pressed
