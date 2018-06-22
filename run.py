
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
	x time.sleep -> 0
	constant frequency runtime
	x Project Speedup
	x automatic port naming Dashboard
	x offline version that auto-runs
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
localLogging = False # 974 -> 34 Hz
telemetry = False
DRIVERINTERFACE = True
includeGPS = True
suppressStdout = 3 # 1 (no suppression), 2, 3 (only data) and 4 (strictest suppression) 
SET_EPOCHTIME = None # seconds per loop
SET_PRINTTIME = 0.3
SET_GPSTIME = 0.9
SHOWDEC_SPEED = 10
SHOWDEC_VOLT = 10
SLEEP = 0.0
SENSOR = False

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
		if debugging: 
			print key.id()
			print key.secret()
		if telemetry: conn = boto.sqs.connect_to_region("eu-west-2", aws_access_key_id = key.getid(), aws_secret_access_key = key.getsecret())

		# Open connection to the gps server
		tn = telnetlib.Telnet("192.168.50.1", 60660)

		# Open connection to the sqs
		while telemetry:
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
if SENSOR: sensordata = sensorPacket()

# Create serial connection for writing to the driver interface
if DRIVERINTERFACE: driverInterface = driverInterface()

# Clear the database before  running
cleardb()

lastLogTime = datetime.now().strftime('%M')
gps_time = time.time()

print "Start main loop."
starttime = datetime.now().strftime('%H:%M:%S.%f')[:-3]
file = open(os.path.join("logs/","separate_"+str(starttime)+".txt"), "a")

stdout = ""
counter = 0.0
totaltime = 0
start_time = time.time()
while(True):
	epoch += 1
	try:
		ctime = datetime.now().strftime('%H:%M:%S.%f')[:-3]
		if debugging: print "Flag 1."
	
		# Collect rpm data to add them to database and send to ground base
#		sensordata.getDummy(ctime)
		if SENSOR: sensordata.fetchData(ctime)

		if extratime: print "--- %s seconds ---" % (time.time() - start_time)

		if debugging: print "Flag 1.1"
		if extratime: print "--- %s seconds ---" % (time.time() - start_time)
		if SENSOR: rpmdata 	= sensordata.getRPMdata()
		if debugging: print "Flag 1.2"
		if extratime: print "--- %s seconds ---" % (time.time() - start_time)
		if SENSOR: throttledata	= sensordata.getThrottledata()
		if debugging: print "Flag 1.3"
		if extratime: print "--- %s seconds ---" % (time.time() - start_time)
		if SENSOR: currentdata 	= sensordata.getCurrentdata()
		if debugging: print "Flag 1.4"
		if extratime: print "--- %s seconds ---" % (time.time() - start_time)
		if SENSOR: voltagedata	= sensordata.getVoltagedata()
		if debugging: print "Flag 1.5"
		if extratime: print "--- %s seconds ---" % (time.time() - start_time)
		
		#oprint start_time - gps_time
		if includeGPS:
			if start_time - gps_time > SET_GPSTIME or  epoch < 5: # 0.9 if locallogging
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
		time.sleep(SLEEP)

		#print str(rpmToKMH(rpmdata.getData(), 0.235)) + " " + str(throttledata.getData()) + " " + str(currentdata.getData()) + " " + str(voltagedata.getData())
	
		if debugging: print "Flag 3."	

		valRPM 		= 0#rpmdata.getData()
		valThrottle 	= 0#throttledata.getData()
		valCurrent 	= '0.00/0.00'#currentdata.getData()
		valVoltage	= 0#int(voltagedata.getData())
		valSpeed = rpmToKMH(float(valRPM), 0.235)

		# Fuck Stephan
		if (valSpeed == 0):
			valSpeedDisplay = valSpeed + 1 
		else:
			valSpeedDisplay = valSpeed * SHOWDEC_SPEED
		if (valVoltage == 0):
			valVoltageDisplay = valVoltage + 1
		else:
			valVoltageDisplay = valVoltage * SHOWDEC_VOLT
		counter = counter + time.time() - start_time
		if DRIVERINTERFACE and counter > SET_PRINTTIME:
			if debugging: print str(valSpeedDisplay) + "," + str(int(valVoltageDisplay))
			driverInterface.getSerial().write("S"+ str(int(1.852 * gpsdata.getSpeed())) +","+str(int(valVoltageDisplay)))

		if debugging: print "Flag 4."
		if extratime: print "--- %s seconds ---" % (time.time() - start_time)

		# Check if 3 minutes have passed to write the log
		timeNow = datetime.now().strftime('%M')
		if localLogging and ( abs(int(timeNow) - int(lastLogTime)) == 3 or abs(int(timeNow) - int(lastLogTime)) == 57):
			writeDBToFile()
			lastLogTime = timeNow

		valCurrent1, valCurrent2 =  valCurrent.split('/')

		file.write(str(epoch) + "\t" + str(valThrottle) + "\t" + str(valRPM) + "\t" + str(valSpeed) + "\t" + valCurrent1 + "\t" + valCurrent2 + \
				"\t" + str(valVoltage) + "\t" + str(1.852 * gpsdata.getSpeed()) + "\t" + str(gpsdata.getLongtitude()) +\
				 "\t" + str(gpsdata.getLattitude()) + "\t%s" % (time.time() - start_time) + "\t" + str(ctime) + "\n")
		if includeGPS and counter>SET_PRINTTIME: 
			print "Epoch = " + str(epoch) + "\tT = " + str(valThrottle) + "\tV = " + str(valSpeed) + "\tI_1 = " + valCurrent1 + "\tI_2 = " + valCurrent2 +\
				"\tU = " + str(valVoltage) + "\tV_GPS = " + str(1.852 * gpsdata.getSpeed()) + "\tLong = " + str(gpsdata.getLongtitude()) +\
				 "\tLat = " + str(gpsdata.getLattitude()) + "\t--- %s seconds ---" % (time.time() - start_time)

		if debugging: print "End of loop."
		totaltime = totaltime + time.time() - start_time
		start_time = time.time()
		if counter>0.3: counter = 0.0		

	except ValueError:
		print "Wrong value for the rpm data!"

#	except AttributeError:
#		print "-----------------------------------------------"

	except KeyboardInterrupt:
		file.close()
		if localLogging: writeDBToFile()
		print "Finished " + str(epoch) + " epochs in %s" % totaltime + " resulting in an average update frequency of %s" % round(epoch / totaltime) + "Hz"
		sys.exit()

