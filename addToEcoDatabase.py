from SensorData import SensorData
from GPS import GPS
import boto.sqs
from boto.sqs.message import Message
import MySQLdb

debugging = False

def addToDatabase(message):
	db = MySQLdb.connect("localhost","root","reverse","ecoData" )
	cursor = db.cursor()

	# Add data from the throttle sensor to the database
	if isinstance(message, SensorData) and message.getSensorId() == "1":
		try: 	
			cursor.execute("""INSERT INTO Throttle (TYPE, DATA, TIMESTAMP) VALUES (%s, %s, %s)""", (message.getMsgType(), message.getData(), message.getTimestamp()))
			db.commit()
			if debugging: print "Throttle data added to database"
		except:
			print "Something went wrong while adding throttle to the database"


	# Add data from the first rpm sensor to the database
	elif isinstance(message, SensorData) and message.getSensorId() == "2":
		try:
			cursor.execute("""INSERT INTO Rpm1 (TYPE, DATA, TIMESTAMP) VALUES (%s, %s, %s)""", (message.getMsgType(), message.getData(), message.getTimestamp()))
			db.commit()
			if debugging: print "Rpm data added to database"
		except:
			print "Something went wrong while adding rpm 1 to the database"

	# Add data from the first current sensor to the database
	elif isinstance(message, SensorData) and message.getSensorId() == "3":
		try:
			cursor.execute("""INSERT INTO Current1 (TYPE, DATA, TIMESTAMP) VALUES (%s, %s, %s)""", (message.getMsgType(), message.getData(), message.getTimestamp()))
			db.commit()
			if debugging: print "Current 1 data added to database"
		except:
			print "Something went wrong while adding current 1 to the database"

	# Add data from the second current sensor to the database
	elif isinstance(message, SensorData) and message.getSensorId() == "4":
		try:
			cursor.execute("""INSERT INTO Current2 (TYPE, DATA, TIMESTAMP) VALUES (%s, %s, %s)""", (message.getMsgType(), message.getData(), message.getTimestamp()))
			db.commit()
			if debugging: print "Current 2 data added to database"
		except:
			print "Something went wrong while adding current 2 to the database"


	# Add data from the first voltage sensor to the database
	elif isinstance(message, SensorData) and message.getSensorId() == "5":
		try:
			cursor.execute("""INSERT INTO Voltage1 (TYPE, DATA, TIMESTAMP) VALUES (%s, %s, %s)""", (message.getMsgType(), message.getData(), message.getTimestamp()))
			db.commit()
			if debugging: print "Voltage 1 data added to database"
		except:
			print "Something went wrong while adding voltage 1 to the database"

	# Add data from the second voltage sensor to the database
	elif isinstance(message, SensorData) and message.getSensorId() == "6":
		try:
			cursor.execute("""INSERT INTO Voltage2 (TYPE, DATA, TIMESTAMP) VALUES (%s, %s, %s)""", (message.getMsgType(), message.getData(), message.getTimestamp()))
			db.commit()
			if debugging: print "Voltage 2 data added to database"
		except:
			print "Something went wrong while adding voltage 2 to the database"

	
	# Add data from the GPS sensor to the database
	elif isinstance(message, GPS):
		try:
			cursor.execute("""INSERT INTO GPS (LONGTITUDE, LATTITUDE, SPEED, TIMESTAMP) VALUES (%s, %s, %s, %s)""", (message.getLongtitude(), message.getLattitude(), message.getSpeed(), message.getTimestamp()))
			db.commit()
			if debugging: print "GPS data added to database"

		except:
			print "Something went wrong while adding GPS to the database"

	elif message is None:
		pass

	else:
		pass

	db.close()
