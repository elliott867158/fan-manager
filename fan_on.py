import RPi.GPIO as GPIO

tran_pin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False) #disable annoying warnings
GPIO.setup(tran_pin, GPIO.OUT)

print ("Turning fan on...")
GPIO.output(tran_pin, GPIO.HIGH)
#print ("Done Press ctrl+C to stop fan")
#while True:
    #try:
        #uselessvar = "useless"
    #except KeyboardInterrupt:
        #print ("Turning off fan...")
        #GPIO.output(tran_pin, GPIO.LOW)
        #print ("Cleaning up Gpio...")
        #GPIO.cleanup()
        #print ("Done")
        #break
    #except SystemExit:
        #print ("SystemExit was called. Turning off fan")
        #GPIO.output(tran_pin, GPIO.LOW)
        #print ("Cleaning up Gpio...")
        #GPIO.cleanup()
        #print ("Done")
        #break