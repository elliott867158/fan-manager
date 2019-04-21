import RPi.GPIO as GPIO #import library with simpler name

tran_pin = 18 #use easier name for pin used

GPIO.setmode(GPIO.BCM) #use BCM pinout
GPIO.setwarnings(False) #disable annoying warnings
GPIO.setup(tran_pin, GPIO.OUT) #set pin to output

GPIO.output(tran_pin, GPIO.HIGH) #set pin to high
