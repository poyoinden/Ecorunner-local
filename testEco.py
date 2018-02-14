import unittest
import sys
import MySQLdb
from writeMessage import writeMessage
from parseMessage import parseMessage
from SensorData import SensorData
from GPS import GPS
from addToEcoDatabase import addToDatabase
from cleardb import cleardb

""" Test class for the sensor data module """
class TestSensorData(unittest.TestCase):

	# Test if the right object is created
	def testTypeOfSensorData(self):
		self.assertTrue(isinstance(SensorData("1", "power", 5, "123.456"), SensorData))

	# Test the get throttle method
	def testGetSensorId(self):
		self.assertEquals(SensorData("1", "power", 5, "123.456").getSensorId(), "1")

	# Test the get display switch method
	def testGetMsgType(self):
		self.assertEquals(SensorData("1", "power", 5, "123.456").getMsgType(), "power")

	# Test the get timestamp method
	def testGetData(self):
		self.assertEquals(SensorData("1", "power", 5, "123.456").getData(), 5)

	# Test the get timestamp method
	def testGetTimeStamp(self):
		self.assertEquals(SensorData("1", "power", 5, "123.456").getTimestamp(), "123.456")

	# Test the toString method
	def testToString(self):
		self.assertEquals(SensorData("1", "power", 5, "123.456").toString(), "SensorId: 1, MessageType: power, Data: 5, timestamp: 123.456")


""" Test class for the gps module """
class TestGPS(unittest.TestCase):

	# Test if the right object is created
	def testTypeOfGPS(self):
		self.assertTrue(isinstance(GPS("1234.567890", "0987.654321", 5.10, "123.456"), GPS))

	# Test the get throttle method
	def testGetLongtitude(self):
		self.assertEquals(GPS("1234.567890", "0987.654321", 5.10, "123.456").getLongtitude(), "1234.567890")

	# Test the get display switch method
	def testGetLattitude(self):
		self.assertEquals(GPS("1234.567890", "0987.654321", 5.10, "123.456").getLattitude(), "0987.654321")

	# Test the get timestamp method
	def testGetSpeed(self):
		self.assertEquals(GPS("1234.567890", "0987.654321", 5.10, "123.456").getSpeed(), 5.10)

	# Test the get timestamp method
	def testGetTimeStamp(self):
		self.assertEquals(GPS("1234.567890", "0987.654321", 5.10, "123.456").getTimestamp(), "123.456")

	# Test the toString method
	def testToString(self):
		self.assertEquals(GPS("1234.567890", "0987.654321", 5.10, "123.456").toString(), "GPS: Longtitude: 1234.567890, Lattitude: 0987.654321, Speed: 5.1, Timestamp: 123.456")


""" Test class for the module addToGBDatabase """
class TestAddToDB(unittest.TestCase):
	
	# Test adding data from the throttle sensor to the database
	def testAddPower1(self):
		# Open connection with the database		
		db = MySQLdb.connect("localhost","root","reverse","ecoData")
		cursor = db.cursor()

		# Add a information to the database
		dr = SensorData("1", "throttle", 7, "123.456.789")
		addToDatabase(dr)

		# Get information from the database
		cursor.execute("SELECT * FROM Throttle")
		result = cursor.fetchone()
		dbId = result[0]
		dbType = result[1]
		dbData = result[2]
		dbTimestamp = result[3]

		# Close the connection and wipe the database
		db.close()
		cleardb()

  	      	self.assertTrue(dbId == 1 and dbType == "power" and dbData == "7" and dbTimestamp == "123.456.789")


	
	# Test adding data from the first rpm sensor to the database
	def testAddRPM1(self):
		# Open connection with the database		
		db = MySQLdb.connect("localhost","root","reverse","ecoData")
		cursor = db.cursor()

		# Add a information to the database
		dr = SensorData("4", "rpm", 7, "123.456.789")
		addToDatabase(dr)

		# Get information from the database
		cursor.execute("SELECT * FROM Rpm1")
		result = cursor.fetchone()
		dbId = result[0]
		dbType = result[1]
		dbData = result[2]
		dbTimestamp = result[3]

		# Close the connection and wipe the database
		db.close()
		cleardb()

  	      	self.assertTrue(dbId == 1 and dbType == "rpm" and dbData == "7" and dbTimestamp == "123.456.789")

		# Test adding data from the first current sensor to the database
	def testAddVoltage1(self):
		# Open connection with the database		
		db = MySQLdb.connect("localhost","root","reverse","ecoData")
		cursor = db.cursor()

		# Add a information to the database
		dr = SensorData("3", "current", 7, "123.456.789")
		addToDatabase(dr)

		# Get information from the database
		cursor.execute("SELECT * FROM Current1")
		result = cursor.fetchone()
		dbId = result[0]
		dbType = result[1]
		dbData = result[2]
		dbTimestamp = result[3]

		# Close the connection and wipe the database
		db.close()
		cleardb()

  	      	self.assertTrue(dbId == 1 and dbType == "current" and dbData == "7" and dbTimestamp == "123.456.789")


	# Test adding data from the second current sensor to the database
	def testAddVoltage1(self):
		# Open connection with the database		
		db = MySQLdb.connect("localhost","root","reverse","ecoData")
		cursor = db.cursor()

		# Add a information to the database
		dr = SensorData("4", "current", 7, "123.456.789")
		addToDatabase(dr)

		# Get information from the database
		cursor.execute("SELECT * FROM Current2")
		result = cursor.fetchone()
		dbId = result[0]
		dbType = result[1]
		dbData = result[2]
		dbTimestamp = result[3]

		# Close the connection and wipe the database
		db.close()
		cleardb()

  	      	self.assertTrue(dbId == 1 and dbType == "current" and dbData == "7" and dbTimestamp == "123.456.789")


	# Test adding data from the first voltage sensor to the database
	def testAddVoltage1(self):
		# Open connection with the database		
		db = MySQLdb.connect("localhost","root","reverse","ecoData")
		cursor = db.cursor()

		# Add a information to the database
		dr = SensorData("5", "voltage", 7, "123.456.789")
		addToDatabase(dr)

		# Get information from the database
		cursor.execute("SELECT * FROM Voltage1")
		result = cursor.fetchone()
		dbId = result[0]
		dbType = result[1]
		dbData = result[2]
		dbTimestamp = result[3]

		# Close the connection and wipe the database
		db.close()
		cleardb()

  	      	self.assertTrue(dbId == 1 and dbType == "voltage" and dbData == "7" and dbTimestamp == "123.456.789")


	# Test adding data from the second voltage sensor to the database
	def testAddVoltage2(self):
		# Open connection with the database		
		db = MySQLdb.connect("localhost","root","reverse","ecoData")
		cursor = db.cursor()

		# Add a information to the database
		dr = SensorData("6", "voltage", 7, "123.456.789")
		addToDatabase(dr)

		# Get information from the database
		cursor.execute("SELECT * FROM Voltage2")
		result = cursor.fetchone()
		dbId = result[0]
		dbType = result[1]
		dbData = result[2]
		dbTimestamp = result[3]

		# Close the connection and wipe the database
		db.close()
		cleardb()

  	      	self.assertTrue(dbId == 1 and dbType == "voltage" and dbData == "7" and dbTimestamp == "123.456.789")


	# Test adding data from the GPS sensor to the database
	def testAddGPS(self):
		# Open connection with the database		
		db = MySQLdb.connect("localhost","root","reverse","ecoData")
		cursor = db.cursor()

		# Add a information to the database
		dr = GPS("1234.567865", "098765.4321", 7.20, "123.456.789")
		addToDatabase(dr)

		# Get information from the database
		cursor.execute("SELECT * FROM GPS")
		result = cursor.fetchone()
		dbId = result[0]
		dbLong = result[1]
		dbLat = result[2]
		dbSpe = result[3]
		dbTimestamp = result[4]

		# Close the connection and wipe the database
		db.close()
		cleardb()

  	      	self.assertTrue(dbId == 1 and dbLong == "1234.567865" and dbLat == "098765.4321" and dbSpe == 7.20 and dbTimestamp == "123.456.789")



""" Test class for the writeMessage module """
class TestWriteMessage(unittest.TestCase):		

	# Test with a correct gps object
	def testCorrectGPS(self):
		gps = GPS(1, 2, 3, 4)
		self.assertEqual(writeMessage(gps), "gp,1,2,3,4")


	# Test with a correct sensor data object
	def testCorrectSensor(self):
		sen = SensorData(1, "power", 2, 3)
		self.assertEqual(writeMessage(sen), "se,1,power,2,3")

if __name__ == '__main__':
    unittest.main()
