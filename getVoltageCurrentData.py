import serial
import time
from SensorData import SensorData
from datetime import datetime
import re

class currentsensor():
	def __init__(self):
		self.ser = serial.Serial(baudrate = 38400, port = 'dev/ttyUSB1', timeout = 0)
		self.cur = -1
		self.tim = datetime.now().strftime('%H:%M:%S.%f')[:-3]

	def getCurrentData(self):
		try:
			while(self.ser.in_waiting):
				incoming = self.ser.readline().rstrip()
				splitUp = re.split(',', incoming)
				self.cur = str(splitUp[0])
				print str(splitUp[0])
				self.tim = datetime.now().strftime('%K:%M:%S.%f')[:-3]
		
			return SensorData('9', 'Current', self.cur, self.tim)
		
		except IndexError:
			print "Wrong current value, nothing sent"			


