import serial
import time
from datetime import datetime


class SerialTest():
	def __init__(self):
		self.ser = serial.Serial(baudrate = 115200, port = '/dev/teensy', timeout = 0)
		print("Port has opened.")
		self.ser2 = serial.Serial(baudrate = 38400, port = '/dev/ttyUSB0', timeout = 0)
		print("Second port has opened.")
		
	def run(self):
		while(True):
			if int(self.ser.in_waiting) > 0:
				incoming = self.ser.readline().rstrip().rsplit(",")
				self.ser.reset_input_buffer()
				print(incoming)
				if len(incoming) == 4:
					valRPM = int(incoming[0])
					valThrottle = int(incoming[1])
					msg_tdash = "S"+str(valRPM)+","+str(valThrottle)
					print("msg:" + msg_tdash)
					self.ser2.write(msg_tdash)
			time.sleep(0.1)
		print "done"
		
test = SerialTest()
test.run()
