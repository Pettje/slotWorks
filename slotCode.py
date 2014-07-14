import RPi.GPIO as GPIO
from time import sleep
import random

GPIO.setmode(GPIO.BCM)

GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(25, GPIO.OUT)

coins = 6
GPIO.output(25,GPIO.LOW)

result = random.randInt(1,9)

jackpot = 10
halfWin = 5
moneyBack = 1

while True:
	sleep(2)

	if result == jackpot or result == halfWin or result == moneyBack:
		GPIO.wait_for_edge(24, GPIO.RISING)
		coins += 1
		
		if result == jackpot:
	 		if coins == 10:
				GPIO.output(25,GPIO.LOW)
				print "jackpot"
			else:
				GPIO.output(25,GPIO.HIGH)
		elif  result == halfWin:
	 		if coins == 5:
				GPIO.output(25,GPIO.LOW)
				print "halfWin"
			else:
				GPIO.output(25,GPIO.HIGH)
		elif result == moneyBack:
			if coins == 1:
				GPIO.output(25,GPIO.LOW)
				print "moneyBack"
			else:
				GPIO.output(25,GPIO.HIGH)
		else:
			GPIO.output(25,GPIO.LOW)
	else:
		GPIO.output(25,GPIO.LOW)
	coins = 6

	






