import serial
import time
from SensorData import SensorData
from datetime import datetime

class throttleSensor():
	def __init__(self):	
		self.ser = serial.Serial(baudrate = 38400, port = '/dev/ttyUSB0', timeout = 0)
		self.throttle = -1
		self.tim = -1
	

	def getThrottledata(self, time):
		try:
			while(self.ser.in_waiting):
				incoming = self.ser.readline().rstrip()
				self.throttle = int(incoming)
				#print "throttle: " + incoming
				self.tim = time
		
			return SensorData('1', 'throttle', self.throttle, self.tim)

		except IndexError:
			print "Wrong current value, nothing sent"

	
	def getSerial(self):
		return self.ser
