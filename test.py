# the sensor has to be connected to pin 1 for power, pin 6 for ground
# and pin 7 for signal(board numbering!).
 
import time, sys,os
import RPi.GPIO as GPIO
 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
 
def action(pin):
#    if GPIO.input(7)==GPIO.HIGH:
    os.system('python sms.py')
    print 'Sensor detected action!'
    return
 
GPIO.add_event_detect(7, GPIO.RISING,callback=action,bouncetime=2000)
#GPIO.add_event_callback(7, action)
 
try:
    while True:
        print 'alive'
        time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit()
