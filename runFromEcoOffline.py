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
from throttleSensor import throttleSensor
from datetime import datetime
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

def rpmToKMH(rpm, wheelCirc):			
	rps = int(rpm) / 60
	speed = rps * wheelCirc * 3.6
	speedToWrite = 1200 + int(round(speed))%100
	
	return speedToWrite


# Create RPM sensor object
rpmsensor = rpmsensor()

# Create Current sensor object
currentsensor = currentsensor()

# Create serial connection for writing to the driver interface
driverInterface = throttleSensor()
wheelCirc = 0.235 * 2 * math.pi

# Clear the database before running
cleardb()

lastLogTime = datetime.now().strftime('%M')
while(True):
	try:
		ctime = datetime.now().strftime('%H:%M:%S.%f')[:-3]

		# Collect rpm data to add them to database and send to ground base
		rpmObject = rpmsensor.getRPMdata(ctime)
		rpm = rpmObject.getData()

		# write the speed in km/h to the screen
		driverInterface.getSerial().write(str(rpmToKMH(rpm, wheelCirc)))
		
		addToDatabase(rpmObject)

		# Collect throttle data to add them to database and send to ground base
		throttleObject = driverInterface.getThrottledata(ctime)
		throttle = throttleObject.getData()

		addToDatabase(throttleObject)

		# Collect current data to add them to database and send to ground base
		currentObject = currentsensor.getCurrentData(ctime)
		current = currentObject.getData()

		addToDatabase(currentObject)	


		# Check if 3 minutes have passed to write the log
		timeNow = datetime.now().strftime('%M')
		if abs(int(timeNow) - int(lastLogTime)) == 3 or abs(int(timeNow) - int(lastLogTime)) == 57:
			writeDBToFile()
			lastLogTime = timeNow

		time.sleep(0.2)

	except ValueError:
		print "Wrong value for the rpm data!"

	except KeyboardInterrupt:
		sys.exit()
