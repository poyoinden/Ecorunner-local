import serial
import time
from SensorData import SensorData
from datetime import datetime

class rpmsensor():
	def __init__(self):	
		self.ser = serial.Serial(baudrate = 115200, port = '/dev/teensy', timeout = 0)
		self.rpm = -1
		self.tim = -1
	

	def getRPMdata(self, time):
		try:
			while(self.ser.in_waiting):
				incoming = self.ser.readline().rstrip()
				print incoming
				self.rpm = incoming		
				self.tim = time
		
			return SensorData('2', 'rpm', self.rpm, self.tim)

		except IndexError:
			print "Wrong RPM value, nothing sent"		

		except ValueError:
			print "wrong RPM value, could not cast to int"
