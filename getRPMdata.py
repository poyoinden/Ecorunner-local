import serial
import time
from SensorData import SensorData
from datetime import datetime
import sys 

class sensorPacket():
	def __init__(self):	
		self.ser = open('/dev/teensy', 'r')
		
		self.rpm = -1
		self.throttle = -1
		self.current = -1
		self.voltage = -1

		self.tim = -1
	
	def fetchData(self, time):
		try:
			print "SensorPacket.fetchData.flag1"
			#print self.ser.is_open
			if self.ser.in_waiting > 0:
				incoming = self.ser.readline().strip().rsplit(",")
				print incoming
				#print "Length:" + str(len(incoming))
	
				self.tim = time
	
#				print "SensorPacket.fetchData.flag2"
				if len(incoming) == 4:
#					print "SensorPacket.fetchData.flag3"
					self.rpm 	= int(incoming[0])
					self.throttle 	= int(incoming[1])
					self.current 	= float(incoming[2])
					self.voltage 	= float(incoming[3])
					return SensorData('0', 'all', [self.rpm, self.throttle, self.current, self.voltage], self.tim)			

#			print "SensorPacket.fetchData.flag4: No data received."
			return

		except IndexError:
			print "Wrong sensor data received, nothing sent"

		except ValueError:
			print "Wrong sensor data received, could not cast to int"

		except:
			e = sys.exc_info()[0]
			print "Something went wrong."
			print "Error: "+str(e)

	def getRPMdata(self):
		return SensorData('1', 'rpm', self.rpm, self.tim)
	def getThrottledata(self):
		return SensorData('2', 'throttle', self.throttle, self.tim)
	def getCurrentdata(self):
		return SensorData('3', 'current', self.current, self.tim)
	def getVoltagedata(self):
		return SensorData('4', 'votlage', self.voltage, self.tim)


