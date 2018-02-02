from __future__ import division
from Instruction import Instruction
from GBInstruction import GBInstruction
from DriverInstruction import DriverInstruction
from StrategyInstruction import StrategyInstruction
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
		conn = boto.sqs.connect_to_region("eu-central-1", aws_access_key_id = "AKIAI5H2RJ4GG4VZGLDQ", aws_secret_access_key = "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")
		tn = telnetlib.Telnet("192.168.50.1", 60660)
		
		# Open connection to the gps server
		while True:
			receiveQueue = conn.get_queue('GB2Eco')
			sendQueue = conn.get_queue('Eco2GB')

			if sendQueue is None or receiveQueue is None:
				print "Connecting to GPS and queue servers..."
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

# Create RPM sensor object
#rpmsensor = rpmsensor()

# Create Current sensor object
currentsensor = currentsensor()

# Create serial connection for writing to the driver interface
#driverInterface = serial.Serial(baudrate = 38400, port = '/dev/ttyUSB1', timeout = 0)
#wheelCirc = 0.235 * 2 * math.pi

# Clear the database before running
cleardb()

while(True):
	try:

		# Collect incoming message and add them to the database
		message = nextMessage(receiveQueue)
		""" To-do: Do something with that message """
		addToDatabase(message)

		
		# Collect gps data to add them to database and send to ground base
		ctime = datetime.now().strftime('%H:%M:%S.%f')[:-3]
		gps = getGPSData(tn, ctime)
		makeMessage(gps, sendQueue)
		addToDatabase(gps)


		# Collect rpm data to add them to database and send to ground base
		#rpmObject = rpmsensor.getRPMdata(ctime)
		
		#try:
			#rpm = rpmObject.getData()
			#print(rpm)
			
			#rps = int(rpm) / 60
			#speed = rps * wheelCirc * 3.6
			#speedToWrite = 1200 + int(round(speed))%100
			# Schrijf de waarde voor de snelheid (km/h) naar het scherm
			#driverInterface.write(str(speedToWrite))
		
		#except ValueError:
			#pass


		#addToDatabase(rpmObject)
		#makeMessage(rpmObject, sendQueue)

		# Collect current data to add them to database and send to ground base
		currentObject = currentsensor.getCurrentData(ctime)
		current = currentObject.getData()

		addToDatabase(currentObject)
		makeMessage(currentObject, sendQueue)		
		

		time.sleep(0.2)

	except KeyboardInterrupt:
		writeDBToFile()
		sys.exit()

