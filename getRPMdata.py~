import serial
import time
from SensorData import SensorData
from datetime import datetime

class rpmsensor():
	def __init__(self):
	
		self.ser = serial.Serial(baudrate = 9600, port = '/dev/ttyUSB0', timeout = 0)
		self.rpm = -1
		self.tim = -1
	

	def getRPMdata(self, time):
		while(self.ser.in_waiting):
			self.rpm = str(self.ser.readline()).rstrip()
			self.rpm.decode(encoding = 'ascii', errors = 'ignore')
			self.tim = time
		
		return SensorData('4', 'rpm', self.rpm, self.tim)
