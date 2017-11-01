import serial
import time
from SensorData import SensorData
from datetime import datetime
import re

class voltagesensor():
	def __init__(self):
		self.ser = serial.Serial(baudrate = 38400, port = 'dev/ttyUSB1', timeout = 0)
		self.vol = -1
		self.tim = datetime.now().strftime('%H:%M:%S.%f')[:-3]

		
	def getVoltageData(self):
		try:
			while(self.ser.in_waiting):
				incoming = self.ser.readline().rstrip()
				splitUp = re.split(',', incoming)
				self.vol = splitUp[1]
				self.tim = datetime.now().strftime('%H:%M:%S.%f')[:-3]

			return SensorData('7', 'Voltage', self.vol, self.tim)

		except IndexError:
			print "Wrong voltage value, nothing sent"
