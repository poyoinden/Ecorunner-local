from __future__ import division
from SensorData import SensorData
from parseMessage import parseMessage
from readMessage import nextMessage
from addToEcoDatabase import addToDatabase
from getGPSData import getGPSData
from cleardb import cleardb
from makeMessage import makeMessage
from sensorPacket import sensorPacket
from writeDBToFile import writeDBToFile
from driverInterface import driverInterface
from datetime import datetime
from rpmToKMH import rpmToKMH
from boto.sqs.message import Message

import sys
import MySQLdb
import re
import time
import socket
import boto.sqs
import telnetlib
import serial
import math
import pprint

"""------------------TO DO----------------------
Implement
	time.sleep -> 0
	constant frequency runtime
	Project Speedup
	automatic port naming Dashboard
	offline version that auto-runs
	get and send GPS data
	automatic write-to-textfile
	multiple points per packet (a0,b0,c0;a1,b1,c1)
---------------------------------------------"""

WHEELRADIUS = 0.235
CIRCUMFERENCE = WHEELRADIUS * 2 * math.pi

while True:
	try:
		# Open connection to the amazon sqs
		conn = boto.sqs.connect_to_region("eu-west-2", aws_access_key_id = "AKIAJAR3NWUEFXUP2DUA", aws_secret_access_key = "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")

		# Open connection to the gps server
		tn = telnetlib.Telnet("192.168.50.1", 60660)

		# Open connection to the sqs
		while True:
			sendQueue = conn.get_queue('Eco2GB')

			if sendQueue is None:
				print "Connecting to the queue..."
				time.sleep(3)	
				continue
			else:
				print "Connected to the GPS and queue servers!"
				break


		break
	
	except EOFError:
		print "Connection to telnet lost, trying again..."
		time.sleep(5)
		continue

	except socket.error:
		print "Connecting to the internet..."
		time.sleep(5)
		continue	
	
	except socket.gaierror:
		print "Connecting to the internet..."
		time.sleep(5)
		continue
print "Going to sleep."
#time.sleep(20)
print "After sleep."

# Create serial connection for writing to the driver interface
driverInterface = driverInterface()

# Clear the database before  running
cleardb()

from random import randrange

lastLogTime = datetime.now().strftime('%M')
print "Start main loop."
while(True):
#	print "Flag 2."
	try:	
		ctime = datetime.now().strftime('%H:%M:%S.%f')[:-3]
		#print "Flag 3."
		# Send separate dataframes per data source, or combined.
		valRPM 		= 58
		valThrottle 	= 12
		driverInterface.getSerial().write("S"+str(valRPM)+","+str(valThrottle))
		#print "Flag 4."
		# Check if 3 minutes have passed to write the log
		timeNow = datetime.now().strftime('%M')
		if abs(int(timeNow) - int(lastLogTime)) == 3 or abs(int(timeNow) - int(lastLogTime)) == 57:
			writeDBToFile()
			lastLogTime = timeNow

		#print "Flag 5."
		time.sleep(0.05)
#		print "End of loop."
	except ValueError:
		print "Wrong value for the rpm data!"

	except AttributeError:
		print "-----------------------------------------------"

	except KeyboardInterrupt:
		writeDBToFile()
		sys.exit()

