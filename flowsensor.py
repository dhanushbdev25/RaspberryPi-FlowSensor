import RPi.GPIO as GPIO
import time, sys
from firebase import firebase
count = 0
tot = 0
pulse_pin = 25
GPIO.setmode(GPIO.BCM)
GPIO.setup(pulse_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
def countPulse1(channel):
        global count
        global tot
        count+=1
     #   print("Number of revolution of wheel of flow sensor:")
      #  print(count)
GPIO.add_event_detect(pulse_pin, GPIO.RISING, callback=countPulse1)

try:
        while True:
                print("Inside while starting")
 		time.sleep(5)
                litre = count/(7.5*60)
                print("Number of litres  used per flow")
                print(litre)
                tot = tot + count
                totlitr = tot/(7.5*60)
                print("Total  litres used ")
                print(totlitr)
                count = 0
                print("Inside while ending")
		 time.sleep(5)
except KeyboardInterrupt:
        print('\ncaught keyboard interrupt!, bye')

GPIO.cleanup()
