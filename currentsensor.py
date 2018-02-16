import serial
import time
from SensorData import SensorData
from datetime import datetime
import re

class currentsensor():
	def __init__(self):
		self.ser = serial.Serial(baudrate = 9600, port = '/dev/ttyUSB0', timeout = 0)
		self.cur = -1
		self.tim = -1

	def getCurrentData(self, time):
		try:
			while(self.ser.in_waiting):
				incoming = self.ser.readline().rstrip()
				print incoming
				self.cur = float(incoming)				
				self.tim = time
		
			return SensorData('3', 'Current', self.cur, self.tim)
		
		except IndexError:
			print "Wrong current value, nothing sent"			
		
		except ValueError:
			print "Wrong value string for the current"
