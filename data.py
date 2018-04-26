import serial
import time
from datetime import datetime

print "starting data.py"
ser = serial.Serial(baudrate = 115200, port = '/dev/teensy', timeout = 1)
while(ser.in_waiting):
	incoming = ser.readline().rstrip()
	print incoming

