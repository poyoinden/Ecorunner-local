from __future__ import division
from SensorData import SensorData
from parseMessage import parseMessage
from readMessage import nextMessage
from addToEcoDatabase import addToDatabase
from getGPSData import getGPSData
from cleardb import cleardb
from makeMessage import makeMessage
from getRPMdata import rpmsensor
from writeDBToFile import writeDBToFile
#from voltagesensor import voltagesensor
from currentsensor import currentsensor
from datetime import datetime
from rpmToKMH import rpmToKMH
import sys
import MySQLdb
import re
import time
import socket
import boto.sqs
from boto.sqs.message import Message
import telnetlib
import serial
import math

while True:
	try:
		# Open connection to the amazon sqs
		conn = boto.sqs.connect_to_region("eu-west-2", aws_access_key_id = "AKIAJAR3NWUEFXUP2DUA", aws_secret_access_key = "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")

		# Open connection to the gps server
		tn = telnetlib.Telnet("192.168.50.1", 60660)

		# Open connection to the gps server
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

print "Connected to the GPS and Queue!"

# Create RPM sensor object
rpmsensor = rpmsensor()

# Create Current sensor object
currentsensor = currentsensor()

# Create serial connection for writing to the driver interface
driverInterface = throttleSensor()

# Clear the database before running
cleardb()

lastLogTime = datetime.now().strftime('%M')
while(True):
	try:
		ctime = datetime.now().strftime('%H:%M:%S.%f')[:-3]

		# Collect rpm data to add them to database and send to ground base
		rpmObject = rpmsensor.getRPMdata(ctime)
		makeMessage(rpmObject, sendQueue)
		addToDatabase(rpmObject)

		# write the speed in km/h to the screen
		driverInterface.getSerial().write(str(rpmToKMH(rpmObject.getData())))
		print "kmh: " + str(rpmToKMH(rpmObject.getData()))

		# Collect throttle data to add them to database and send to ground base
		throttleObject = driverInterface.getThrottledata(ctime)
		makeMessage(throttleObject, sendQueue)	
		addToDatabase(throttleObject)

		# Collect current data to add them to database and send to ground base
		currentObject = currentsensor.getCurrentData(ctime)
		makeMessage(currentObject, sendQueue)
		addToDatabase(currentObject)


		# Check if 3 minutes have passed to write the log
		timeNow = datetime.now().strftime('%M')
		if abs(int(timeNow) - int(lastLogTime)) == 3 or abs(int(timeNow) - int(lastLogTime)) == 57:
			writeDBToFile()
			lastLogTime = timeNow

		time.sleep(0.2)

	except ValueError:
		print "Wrong value for the rpm data!"

	except AttributeError:
		print "-----------------------------------------------"

	except KeyboardInterrupt:
		writeDBToFile()
		sys.exit()

