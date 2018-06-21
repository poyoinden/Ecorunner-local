import serial
import time
from datetime import datetime
import time

class SerialTest():
	def __init__(self):
		self.ser = serial.Serial(baudrate = 115200, port = '/dev/teensy', timeout = 0)
		print("Port has opened.")

	def run(self):
		while(True):
			time.sleep(0.5)
			if int(self.ser.in_waiting) > 0:
				incoming = self.ser.readline().rstrip()
				self.ser.reset_input_buffer()
				print(incoming)
		print "done"

test = SerialTest()
test.run()
