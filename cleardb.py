import MySQLdb

def cleardb():
	# Clear all data from every table
	db = MySQLdb.connect("localhost","root","reverse","ecoData")
	cursor = db.cursor()
	cursor.execute("""TRUNCATE TABLE Throttle""")
	cursor.execute("""TRUNCATE TABLE Rpm1""")
	cursor.execute("""TRUNCATE TABLE Voltage1""")
	cursor.execute("""TRUNCATE TABLE Voltage2""")
	cursor.execute("""TRUNCATE TABLE Current1""")
	cursor.execute("""TRUNCATE TABLE Current2""")
	cursor.execute("""TRUNCATE TABLE GPS""")
	db.close()

