import RPi.GPIO as GPIO
import time
from lib import motor
from socket import *
import sys
import select

GPIO.setmode(GPIO.BCM)

motors = [
	motor.Motor( 7, 8 ),
	motor.Motor( 9, 10 ),
]

state = [ 0, 0, 0, 0 ]

try:
	address = ('0.0.0.0', 33333)
	server_socket = socket(AF_INET, SOCK_DGRAM)
	server_socket.bind(address)

	print "Listening ..."

	while(1):

	    data, addr = server_socket.recvfrom(1024)
	    [ a, b, c, d ] = map( bool, map( int, data.strip().split("|") ) )

	    # print "Received directions: ", [ a, b, c, d ]

	    if a != state[0] or b != state[1]:
	    	motors[0].send( a, b )

	    if c != state[2] or d != state[3]:
	    	motors[1].send( c, d )

	    state = [ a, b, c, d ]

except KeyboardInterrupt:  	
	
	pass

finally:  
	
	motors[0].stop()
	motors[1].stop()

	print "Cleaning GPIO status ..."

	GPIO.cleanup()