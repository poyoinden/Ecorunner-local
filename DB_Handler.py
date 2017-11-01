from Instruction import Instruction
from GBInstruction import GBInstruction
from DriverInstruction import DriverInstruction
from StrategyInstruction import StrategyInstruction
from SensorData import SensorData
from parseMessage import parseMessage
from Eco2GB import sensorMessage
from Eco2GB import driverMessage
from readMessage import nextMessage
from addToEcoDatabase import addToDatabase
import MySQLdb
import re
import time
import boto.sqs
from boto.sqs.message import Message
from getGPSData import getTimeLonLatSpe

def getSensorDataFromPollersToDB(tn, db, cursor):
	# get the list from Poller 1
	# get the list from Poller 2
	# get the list from GPS Socket
	getGPS(tn)
	# Make a message and send everything to GB
	# Write all values from all lists to the database
	
	# Close database connection
	# Close when ...?
