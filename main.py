import RPi.GPIO as GPIO
import time
from lib import car

GPIO.setmode(GPIO.BCM)

c = car.Car( [ 7, 8 ], [ 9, 10 ] )

try:  
	while True:
		c.forward()
		
		c.steer( car.Car.STEER_LEFT )
		time.sleep( 0.5 )
		c.steer( car.Car.STEER_NONE )

		time.sleep( 3.0 )

		c.backward()

		time.sleep( 3.0 )

except KeyboardInterrupt:  	
	
	pass

finally:  
	print "Cleaning GPIO status ..."
	
	c.stop()
	
	GPIO.cleanup()