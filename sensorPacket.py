import serial
import time
from SensorData import SensorData
from datetime import datetime
import sys 
import random

debugging = False

class sensorPacket():
	def __init__(self):	
		#self.ser = open('/dev/teensy', 'r')
		self.ser = serial.Serial(baudrate = 115200, port = '/dev/teensy', timeout = 0)		
		print "Teensy USB connection initialized"
		
		self.rpm = -1
		self.throttle = -1
		self.current = -1
		self.voltage = -1

		self.tim = -1
	
	def fetchData(self, time):
		if debugging: print "SensorPacket.fetchData.flag0"
		try:
			if debugging: print "SensorPacket.fetchData.flag1"
			if int(self.ser.in_waiting) > 0:
				incoming = self.ser.readline().strip().rsplit(",")
				if incoming == None:
					print "Incoming is Null"
				self.ser.reset_input_buffer()

				print incoming
				#print "Length:" + str(len(incoming))

				self.tim = time	
	
				if debugging: print "SensorPacket.fetchData.flag2"
				if len(incoming) == 4:
					#print "SensorPacket.fetchData.flag3"
					self.rpm 	= int(incoming[0])
					self.throttle 	= int(incoming[1])
					self.current 	= float(incoming[2])
					self.voltage 	= float(incoming[3])
					print incoming
					return SensorData('0', 'all', [self.rpm, self.throttle, self.current, self.voltage], self.tim)			

			return

		except IndexError:
			print "Wrong sensor data received, nothing sent"

		except ValueError:
			print "Wrong sensor data received, could not cast to int"

#		except:
#			e = sys.exc_info()[0]
#			print "Something went wrong."
#			print "Error: "+str(e)

	def getDummy(self, ctime):
		self.rpm 	= int(random.randint(0,450))#int(incoming[0])
		self.throttle 	= int(random.randint(0,100))#int(incoming[1])
		self.current 	= float(random.uniform(0,1)*20)#float(incoming[2])
		self.voltage 	= float(random.uniform(0,1)*30)#float(incoming[3])
		return

	def getRPMdata(self):
		return SensorData('2', 'rpm', self.rpm, self.tim)
	def getThrottledata(self):
		return SensorData('1', 'throttle', self.throttle, self.tim)
	def getCurrentdata(self):
		return SensorData('3', 'current', self.current, self.tim)
	def getVoltagedata(self):
		return SensorData('5', 'votlage', self.voltage, self.tim)


