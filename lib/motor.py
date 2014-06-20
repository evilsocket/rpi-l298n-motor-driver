import RPi.GPIO as GPIO

class Motor:
  def __init__(self, pin_a, pin_b):
    print "Creating Motor instance [%d,%d]" % ( pin_a, pin_b )

    self.pin_a    = pin_a
    self.pin_b    = pin_b
  
    # make sure both pin are configured for output
    GPIO.setup( self.pin_a, GPIO.OUT )
    GPIO.setup( self.pin_b, GPIO.OUT )
    # and make sure the motor is stopped
    self.stop()

  # simple method to control both ports at once
  def send( self, a, b ):
    print "Motor [%d,%d] -> %d %d" % ( self.pin_a, self.pin_b, a, b )

    GPIO.output( self.pin_a, GPIO.HIGH if a == True else GPIO.LOW )
    GPIO.output( self.pin_b, GPIO.HIGH if b == True else GPIO.LOW )

  def stop(self):
    print "Stopping motor [%d,%d] ..." % ( self.pin_a, self.pin_b )
    self.send( False, False )

  def forward(self):
    print "Motor [%d,%d] going forward ..." % ( self.pin_a, self.pin_b )
    self.send( True, False )

  def backward(self):
    print "Motor [%d,%d] going backward ..." % ( self.pin_a, self.pin_b )    
    self.send( False, True )
