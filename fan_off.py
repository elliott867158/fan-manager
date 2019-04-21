import RPi.GPIO #inport GPIO library
RPi.GPIO.setwarnings(False) #disable warnings
RPi.GPIO.setmode(RPi.GPIO.BCM) #set mode to bcm pinout
RPi.GPIO.setup(18, RPi.GPIO.OUT) #set pin as output
RPi.GPIO.output(18, RPi.GPIO.LOW) #set pin to low
RPi.GPIO.cleanup() #set all pins to default(input)
