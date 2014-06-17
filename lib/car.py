import motor

class Car:
	STEER_LEFT  = 1
	STEER_RIGHT = 2
	STEER_NONE  = 0

	def __init__( self, acc_pins, steerin_pins ):
		self.accelerator = motor.Motor( acc_pins[0], acc_pins[1] )
		self.steering = motor.Motor( steerin_pins[0], steerin_pins[1] )

	def forward(self):
		print "Car going forward ..."
		self.accelerator.forward()

	def backward(self):
		print "Car going backward ..."
		self.accelerator.backward()

	def stop(self):
		print "Car stopping ..."
		self.accelerator.stop()
		self.steering.stop()

	def steer( self, where ):
		if where == self.STEER_LEFT:
			print "Car turning left ..."
			self.steering.forward()
		elif where == self.STEER_RIGHT:
			print "Car turning right ..."
			self.steering.backward()
		else:
			self.steering.stop()