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
import key

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
extratime = False
localLogging = True
telemetry = False
DRIVERINTERFACE = True
includeGPS = True
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
#		print key.id()
#		print key.secret()
		#conn = boto.sqs.connect_to_region("eu-west-2", aws_access_key_id = key.getid(), aws_secret_access_key = key.getsecret())

		# Open connection to the gps server
		tn = telnetlib.Telnet("192.168.50.1", 60660)

		# Open connection to the sqs
		while False:
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

		if extratime: print "--- %s seconds ---" % (time.time() - start_time)

		if debugging: print "Flag 1.1"
		if extratime: print "--- %s seconds ---" % (time.time() - start_time)
		rpmdata 	= sensordata.getRPMdata()
		if debugging: print "Flag 1.2"
		if extratime: print "--- %s seconds ---" % (time.time() - start_time)
		throttledata	= sensordata.getThrottledata()
		if debugging: print "Flag 1.3"
		if extratime: print "--- %s seconds ---" % (time.time() - start_time)
		currentdata 	= sensordata.getCurrentdata()
		if debugging: print "Flag 1.4"
		if extratime: print "--- %s seconds ---" % (time.time() - start_time)
		voltagedata	= sensordata.getVoltagedata()
		if debugging: print "Flag 1.5"
		if extratime: print "--- %s seconds ---" % (time.time() - start_time)
		
		#oprint start_time - gps_time
		if includeGPS:
			if start_time - gps_time > 0.7 or  epoch < 5:
				gpsdata	= getGPSData(tn, ctime)
				gps_time = start_time
			else:
				gpsdata.updateTimestamp(ctime)

		if debugging: print "Flag 2."
		if extratime: print "--- %s seconds ---" % (time.time() - start_time)


		# Send separate dataframes per data source, or combined.
		#with suppress_stdout():
		if telemetry: makeMessage(rpmdata, 		sendQueue)		
		if localLogging: addToDatabase(rpmdata)
		if extratime: print "--- %s seconds ---" % (time.time() - start_time)
		if telemetry: makeMessage(throttledata, 	sendQueue)		
		if localLogging: addToDatabase(throttledata)
		if extratime: print "--- %s seconds ---" % (time.time() - start_time)
		if telemetry: makeMessage(currentdata, 	sendQueue)		
		if localLogging: addToDatabase(currentdata)
		if extratime: print "--- %s seconds ---" % (time.time() - start_time)
		if telemetry: makeMessage(voltagedata, 	sendQueue)		
		if localLogging: addToDatabase(voltagedata)
		if extratime: print "--- %s seconds ---" % (time.time() - start_time)
		if (telemetry and includeGPS): makeMessage(gpsdata, 		sendQueue)		
		if (localLogging and includeGPS): addToDatabase(gpsdata)

		if extratime: print "--- %s seconds ---" % (time.time() - start_time)

		print str(rpmToKMH(rpmdata.getData(), 0.235)) + " " + str(throttledata.getData()) + " " + str(currentdata.getData()) + " " + str(voltagedata.getData())
		if includeGPS: print str(gpsdata.getSpeed()) + "\t" + str(gpsdata.getLongtitude()) + " " + str(gpsdata.getLattitude())
	
		if debugging: print "Flag 3."	
		valRPM 		= rpmdata.getData()
		valThrottle 	= throttledata.getData()
		valCurrent 	= currentdata.getData()
		valVoltage	= int(voltagedata.getData())
		valSpeed = rpmToKMH(valRPM, 0.235)

	#	try:
#			valSpeedFromGPS = int(gpsdata.getSpeed())
#		except:
		if (valSpeed == 0):
			valSpeed = valSpeed + 1 
		if (valVoltage == 0):
			valVoltage = valVoltage + 1
		if DRIVERINTERFACE:
			driverInterface.getSerial().write("S"+ str(valSpeed) +","+str(int(valVoltage)))
		if debugging: print "Flag 4."
		if extratime: print "--- %s seconds ---" % (time.time() - start_time)

		# Check if 3 minutes have passed to write the log
		timeNow = datetime.now().strftime('%M')
		if abs(int(timeNow) - int(lastLogTime)) == 3 or abs(int(timeNow) - int(lastLogTime)) == 57:
			writeDBToFile()
			lastLogTime = timeNow

		# print_epoch_time_millis(ctime, epoch)
		print "--- %s seconds ---" % (time.time() - start_time)
		if debugging:  print "Flag 5."
		time.sleep(0.01)
		if debugging: print "End of loop."
		

	except ValueError:
		print "Wrong value for the rpm data!"

#	except AttributeError:
#		print "-----------------------------------------------"

	except KeyboardInterrupt:
		writeDBToFile()
		print str(epochs) + "epochs finished."
		sys.exit()

