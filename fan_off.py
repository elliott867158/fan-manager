import RPi.GPIO
RPi.GPIO.setwarnings(False)
RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(18, RPi.GPIO.OUT)
RPi.GPIO.output(18, RPi.GPIO.LOW)
RPi.GPIO.cleanup()