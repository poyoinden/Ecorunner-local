from Instruction import Instruction
from GBInstruction import GBInstruction
from DriverInstruction import DriverInstruction
from StrategyInstruction import StrategyInstruction
from SensorData import SensorData
from GPS import GPS
import boto.sqs
from boto.sqs.message import Message
import MySQLdb


def addToDatabase(message):
	db = MySQLdb.connect("localhost","root","reverse","ecoData" )
	cursor = db.cursor()

		# Add a driver instruction to the database
	if isinstance(message, DriverInstruction):
		try:
			cursor.execute("""INSERT INTO DriverInstructions (THROTTLE, DISPLAYSWITCH, TIMESTAMP) VALUES (%s, %s, %s)""", (message.getThrottle(), message.getDisplaySwitch(), message.getTimestamp()))
			db.commit()
			print message.getType() +  " data added to database"
		except:
			print "Something went wrong while adding driver instruction to the database" 
	
	# Add a gb instruction to the database
	if isinstance(message, GBInstruction):
		try:
			cursor.execute("""INSERT INTO GBInstructions (FCPOWER, THROTTLEADVICE, STEERADVICE, MOTORSETTINGS, TIMESTAMP) VALUES (%s, %s, %s, %s, %s)""", (message.getFcPower(), message.getThrottleAdv(), message.getSteerAdv(), message.getMotorSet(), message.getTimestamp()))
			db.commit()
			print message.getType() +  " data added to database"
		except:
			print "Something went wrong while adding gb instruction to the database" 


	# Add a strategy instruction to the database
	if isinstance(message, StrategyInstruction):
		try:
			cursor.execute("""INSERT INTO StrategyInstructions (FCPOWER, THROTTLEADVICE, MOTORSETTINGS, TIMESTAMP) VALUES (%s, %s, %s, %s)""", (message.getFcPower(), message.getThrottleAdv(), message.getMotorSet(), message.getTimestamp()))
			db.commit()
			print message.getType() +  " data added to database"
		except:
			print "Something went wrong while adding strategy instruction to the database" 
	
	# Add data from the first power sensor to the database
	elif isinstance(message, SensorData) and message.getSensorId() == "1":
		try: 	
			cursor.execute("""INSERT INTO Power1 (TYPE, DATA, TIMESTAMP) VALUES (%s, %s, %s)""", (message.getMsgType(), message.getData(), message.getTimestamp()))
			db.commit()
			print "Power 1 data added to database"
		except:
			print "Something went wrong while adding power 1 to the database"

	# Add data from the second power sensor to the database
	elif isinstance(message, SensorData) and message.getSensorId() == "2":
		try:
			cursor.execute("""INSERT INTO Power2 (TYPE, DATA, TIMESTAMP) VALUES (%s, %s, %s)""", (message.getMsgType(), message.getData(), message.getTimestamp()))
			db.commit()
			print "Power 2 data added to database"
		except:
			print "Something went wrong while adding power 2 to the database"

	# Add data from the third power sensor to the database
	elif isinstance(message, SensorData) and message.getSensorId() == "3":
		try:
			cursor.execute("""INSERT INTO Power3 (TYPE, DATA, TIMESTAMP) VALUES (%s, %s, %s)""", (message.getMsgType(), message.getData(), message.getTimestamp()))
			db.commit()
			print "Power 3 data added to database"
		except:
			print "Something went wrong while adding power 3 to the database"

	# Add data from the first rpm sensor to the database
	elif isinstance(message, SensorData) and message.getSensorId() == "4":
		try:
			cursor.execute("""INSERT INTO Rpm1 (TYPE, DATA, TIMESTAMP) VALUES (%s, %s, %s)""", (message.getMsgType(), message.getData(), message.getTimestamp()))
			db.commit()
			print "Rpm data added to database"
		except:
			print "Something went wrong while adding rpm 1 to the database"

	# Add data from the second rpm sensor to the database
	elif isinstance(message, SensorData) and message.getSensorId() == "5":
		try:
			cursor.execute("""INSERT INTO Rpm2 (TYPE, DATA, TIMESTAMP) VALUES (%s, %s, %s)""", (message.getMsgType(), message.getData(), message.getTimestamp()))
			db.commit()
			print "Rpm 2 data added to database"
		except:
			print "Something went wrong while adding rpm 2 to the database"

	# Add data from the third rpm sensor to the database
	elif isinstance(message, SensorData) and message.getSensorId() == "6":
		try:
			cursor.execute("""INSERT INTO Rpm3 (TYPE, DATA, TIMESTAMP) VALUES (%s, %s, %s)""", (message.getMsgType(), message.getData(), message.getTimestamp()))
			db.commit()
			print "Rpm 3 data added to database"
		except:
			print "Something went wrong while adding rpm 3 to the database"

	# Add data from the first voltage sensor to the database
	elif isinstance(message, SensorData) and message.getSensorId() == "7":
		try:
			cursor.execute("""INSERT INTO Voltage1 (TYPE, DATA, TIMESTAMP) VALUES (%s, %s, %s)""", (message.getMsgType(), message.getData(), message.getTimestamp()))
			db.commit()
			print "Voltage 1 data added to database"
		except:
			print "Something went wrong while adding voltage 1 to the database"

	# Add data from the second voltage sensor to the database
	elif isinstance(message, SensorData) and message.getSensorId() == "8":
		try:
			cursor.execute("""INSERT INTO Voltage2 (TYPE, DATA, TIMESTAMP) VALUES (%s, %s, %s)""", (message.getMsgType(), message.getData(), message.getTimestamp()))
			db.commit()
			print "Voltage 2 data added to database"
		except:
			print "Something went wrong while adding voltage 2 to the database"

	# Add data from the first current sensor to the database
	elif isinstance(message, SensorData) and message.getSensorId() == "9":
		try:
			cursor.execute("""INSERT INTO Current1 (TYPE, DATA, TIMESTAMP) VALUES (%s, %s, %s)""", (message.getMsgType(), message.getData(), message.getTimestamp()))
			db.commit()
			print "Current 1 data added to database"
		except:
			print "Something went wrong while adding current 1 to the database"

	# Add data from the second current sensor to the database
	elif isinstance(message, SensorData) and message.getSensorId() == "10":
		try:
			cursor.execute("""INSERT INTO Current2 (TYPE, DATA, TIMESTAMP) VALUES (%s, %s, %s)""", (message.getMsgType(), message.getData(), message.getTimestamp()))
			db.commit()
			print "Current 2 data added to database"
		except:
			print "Something went wrong while adding current 2 to the database"

	
	# Add data from the GPS sensor to the database
	elif isinstance(message, GPS):
		try:
			cursor.execute("""INSERT INTO GPS (LONGTITUDE, LATTITUDE, SPEED, TIMESTAMP) VALUES (%s, %s, %s, %s)""", (message.getLongtitude(), message.getLattitude(), message.getSpeed(), message.getTimestamp()))
			db.commit()
			print "GPS data added to database"

		except:
			print "Something went wrong while adding GPS to the database"

	elif message is None:
		pass

	else:
		pass

	db.close()
