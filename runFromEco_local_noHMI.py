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
	x get and send GPS data
	x automatic write-to-textfile
	multiple points per packet (a0,b0,c0;a1,b1,c1)
	x print loop times
	x log loop times
	x fixate frequency of GPS data and solve timestamp problem
---------------------------------------------"""

WHEELRADIUS = 0.235
CIRCUMFERENCE = WHEELRADIUS * 2 * math.pi
debugging = False
localLogging = True
telemetry = False
DRIVERINTERFACE = False
suppressStdout = 3 # 1 (no suppression), 2, 3 (only data) and 4 (strictest suppression) 

from contextlib import contextmanager
import sys, os

@contextmanager
def suppress_stdout():
	with open(os.devnull, "w") as devnull:
		old_stdout = sys.stdout
		sys.stdout = devnull
		try:
			yield
		finally:
			sys.stdout = old_stdout

epoch = 0 
def print_epoch_time_millis(old_t, epoch):
	new_t = datetime.now().strftime('%H:%M:%S.%f')[:-3]
	dt = (int(new_t) - int(old_t)).total_seconds() * 1000.0
	print "Epoch %d: \t %s seconds" % (dt, epoch)
	return

while True:
	try:
		# Open connection to the amazon sqs
		conn = boto.sqs.connect_to_region("eu-west-2", aws_access_key_id = "AKIAIL7GJX2LR33WW3AA", aws_secret_access_key = "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")

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

# Create sensor data object
sensordata = sensorPacket()

# Create serial connection for writing to the driver interface
if DRIVERINTERFACE: driverInterface = driverInterface()

# Clear the database before  running
cleardb()

lastLogTime = datetime.now().strftime('%M')
gps_time = time.time()

print "Start main loop."
while(True):
	start_time = time.time()
	epoch += 1
	try:
		ctime = datetime.now().strftime('%H:%M:%S.%f')[:-3]
		if debugging: print "Flag 1."
	
		# Collect rpm data to add them to database and send to ground base
#		sensordata.getDummy(ctime)
		sensordata.fetchData(ctime)

		if debugging: print "Flag 1.1"
		rpmdata 	= sensordata.getRPMdata()
		if debugging: print "Flag 1.2"
		throttledata	= sensordata.getThrottledata()
		if debugging: print "Flag 1.3"
		currentdata 	= sensordata.getCurrentdata()
		if debugging: print "Flag 1.4"
		voltagedata	= sensordata.getVoltagedata()
		if debugging: print "Flag 1.5"
		

		print start_time - gps_time

		if start_time - gps_time > 1.2 or  epoch < 5:
			gpsdata	= getGPSData(tn, ctime)
			gps_time = start_time
		else:
			gpsdata.updateTimestamp(ctime)

		if debugging: print "Flag 2."

		# Send separate dataframes per data source, or combined.
		#with suppress_stdout():
		if telemetry: makeMessage(rpmdata, 		sendQueue)		
		if localLogging: addToDatabase(rpmdata)
		if telemetry: makeMessage(throttledata, 	sendQueue)		
		if localLogging: addToDatabase(throttledata)
		if telemetry: makeMessage(currentdata, 	sendQueue)		
		if localLogging: addToDatabase(currentdata)
		if telemetry: makeMessage(voltagedata, 	sendQueue)		
		if localLogging: addToDatabase(voltagedata)
		if telemetry: makeMessage(gpsdata, 		sendQueue)		
		if localLogging: addToDatabase(gpsdata)

		print str(rpmdata.getData()) + " " + str(throttledata.getData()) + " " + str(gpsdata.getLongtitude()) + " " + str(gpsdata.getLattitude())
	
		if debugging: print "Flag 3."	
		valRPM 		= rpmdata.getData()
		valThrottle 	= throttledata.getData()
		if DRIVERINTERFACE:
			driverInterface.getSerial().write("S"+str(valRPM)+","+str(valThrottle))
		if debugging: print "Flag 4."

		# Check if 3 minutes have passed to write the log
		timeNow = datetime.now().strftime('%M')
		if abs(int(timeNow) - int(lastLogTime)) == 3 or abs(int(timeNow) - int(lastLogTime)) == 57:
			writeDBToFile()
			lastLogTime = timeNow

		# print_epoch_time_millis(ctime, epoch)
		print "--- %s seconds ---" % (time.time() - start_time)
		if debugging:  print "Flag 5."
		time.sleep(0.03)
		if debugging: print "End of loop."
		

	except ValueError:
		print "Wrong value for the rpm data!"

#	except AttributeError:
#		print "-----------------------------------------------"

	except KeyboardInterrupt:
		writeDBToFile()
		sys.exit()

