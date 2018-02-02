import MySQLdb
import datetime
import os
import os.path

def writeDBToFile():

	# Open database connection
	db = MySQLdb.connect("localhost","root","reverse","ecoData" )
	cursor = db.cursor()

	# Set the name of the output file to a timestamp
	date = datetime.date.today().strftime('%d-%m-%y,')
	time = datetime.datetime.now().strftime('%H:%M:%S')


	save_path = '/home/pi/Gerda/logs'
	name = date + time + ".txt"

	completeName = os.path.join(save_path, name)

	output = open(completeName, "w")

	# Check the driver commands in the database
	sql = "SELECT * FROM DriverInstructions"

	try:
	   # Execute the SQL command
	   cursor.execute(sql)
	   # Fetch all the rows in a list of lists.
	   results = cursor.fetchall()
	   print>>output, "Driver instructions:"
	   for row in results:
	      i_id = row[0]
	      throttle = row[1]
	      displayswitch = row[2]
	      timestamp = row[3]
	      # Now print fetched result
	      print>>output, "%s, %s, %s, %s" % \
		     (i_id, throttle, displayswitch, timestamp)

	   print>>output, ""

	except:
	   print "Error: unable to fetch data"


	# Check the strategy commands in the database
	sql = "SELECT * FROM StrategyInstructions"

	try:
	   # Execute the SQL command
	   cursor.execute(sql)
	   # Fetch all the rows in a list of lists.
	   results = cursor.fetchall()
	   print>>output, "Strategy instructions:"
	   for row in results:
	     i_id = row[0]
	     fcpower = row[1]
	     throttleadv = row[2]
	     motorset = row[3]
	     timestamp = row[4]
	     # Now print fetched result
	     print>>output, "%s, %s, %s, %s, %s" % \
		    (i_id, fcpower, throttleadv, motorset, timestamp)

	   print>>output, ""

	except:
	   print "Error: unable to fetch data"

	# Check the strategy commands in the database
	sql = "SELECT * FROM Power1"

	try:
	   # Execute the SQL command
	   cursor.execute(sql)
	   # Fetch all the rows in a list of lists.
	   results = cursor.fetchall()
	   print>>output, "Power 1:"
	   for row in results:
	     s_id = row[0]
	     s_type = row[1]
	     data = row[2]
	     timestamp = row[3]
	     # Now print fetched result
	     print>>output, "%s, %s, %s, %s" % \
		    (s_id, s_type, data, timestamp)

	   print>>output, ""

	except:
	   print "Error: unable to fetch data"


	# Check the strategy commands in the database
	sql = "SELECT * FROM Power2"

	try:
	   # Execute the SQL command
	   cursor.execute(sql)
	   # Fetch all the rows in a list of lists.
	   results = cursor.fetchall()
	   print>>output, "Power 2:"
	   for row in results:
	     s_id = row[0]
	     s_type = row[1]
	     data = row[2]
	     timestamp = row[3]
	     # Now print fetched result
	     print>>output, "%s, %s, %s, %s" % \
		    (s_id, s_type, data, timestamp)

	   print>>output, ""

	except:
	   print "Error: unable to fetch data"

	# Check the strategy commands in the database
	sql = "SELECT * FROM Power3"

	try:
	   # Execute the SQL command
	   cursor.execute(sql)
	   # Fetch all the rows in a list of lists.
	   results = cursor.fetchall()
	   print>>output, "Power 3:"
	   for row in results:
	     s_id = row[0]
	     s_type = row[1]
	     data = row[2]
	     timestamp = row[3]
	     # Now print fetched result
	     print>>output, "%s, %s, %s, %s" % \
		    (s_id, s_type, data, timestamp)

	   print>>output, ""

	except:
	   print "Error: unable to fetch data"


	# Check the strategy commands in the database
	sql = "SELECT * FROM Rpm1"

	try:
	   # Execute the SQL command
	   cursor.execute(sql)
	   # Fetch all the rows in a list of lists.
	   results = cursor.fetchall()
	   print>>output, "Rpm 1:"
	   for row in results:
	     s_id = row[0]
	     s_type = row[1]
	     data = row[2]
	     timestamp = row[3]
	     # Now print fetched result
	     print>>output, "%s, %s, %s, %s" % \
		    (s_id, s_type, data, timestamp)

	   print>>output, ""

	except:
	   print "Error: unable to fetch data"

	# Check the strategy commands in the database
	sql = "SELECT * FROM Rpm2"

	try:
	   # Execute the SQL command
	   cursor.execute(sql)
	   # Fetch all the rows in a list of lists.
	   results = cursor.fetchall()
	   print>>output, "Rpm 2:"
	   for row in results:
	     s_id = row[0]
	     s_type = row[1]
	     data = row[2]
	     timestamp = row[3]
	     # Now print fetched result
	     print>>output, "%s, %s, %s, %s" % \
		    (s_id, s_type, data, timestamp)

	   print>>output, ""

	except:
	   print "Error: unable to fetch data"

	# Check the strategy commands in the database
	sql = "SELECT * FROM Rpm3"

	try:
	   # Execute the SQL command
	   cursor.execute(sql)
	   # Fetch all the rows in a list of lists.
	   results = cursor.fetchall()
	   print>>output, "Rpm 3:"
	   for row in results:
	     s_id = row[0]
	     s_type = row[1]
	     data = row[2]
	     timestamp = row[3]
	     # Now print fetched result
	     print>>output, "%s, %s, %s, %s" % \
		    (s_id, s_type, data, timestamp)

	   print>>output, ""

	except:
	   print "Error: unable to fetch data"

	# Check the strategy commands in the database
	sql = "SELECT * FROM Voltage1"

	try:
	   # Execute the SQL command
	   cursor.execute(sql)
	   # Fetch all the rows in a list of lists.
	   results = cursor.fetchall()
	   print>>output, "Voltage 1:"
	   for row in results:
	     s_id = row[0]
	     s_type = row[1]
	     data = row[2]
	     timestamp = row[3]
	     # Now print fetched result
	     print>>output, "%s, %s, %s, %s" % \
		    (s_id, s_type, data, timestamp)

	   print>>output, ""

	except:
	   print "Error: unable to fetch data"

	# Check the strategy commands in the database
	sql = "SELECT * FROM Voltage2"

	try:
	   # Execute the SQL command
	   cursor.execute(sql)
	   # Fetch all the rows in a list of lists.
	   results = cursor.fetchall()
	   print>>output, "Voltage 2:"
	   for row in results:
	     s_id = row[0]
	     s_type = row[1]
	     data = row[2]
	     timestamp = row[3]
	     # Now print fetched result
	     print>>output, "%s, %s, %s, %s" % \
		    (s_id, s_type, data, timestamp)

	   print>>output, ""

	   
	except:
	   print "Error: unable to fetch data"

	# Check the strategy commands in the database
	sql = "SELECT * FROM Current1"

	try:
	   # Execute the SQL command
	   cursor.execute(sql)
	   # Fetch all the rows in a list of lists.
	   results = cursor.fetchall()
	   print>>output, "Current 1"
	   for row in results:
	     s_id = row[0]
	     s_type = row[1]
	     data = row[2]
	     timestamp = row[3]
	     # Now print fetched result
	     print>>output, "%s, %s, %s, %s" % \
		    (s_id, s_type, data, timestamp)

	   print>>output, ""

	except:
	   print "Error: unable to fetch data"

	# Check the strategy commands in the database
	sql = "SELECT * FROM Current2"

	try:
	   # Execute the SQL command
	   cursor.execute(sql)
	   # Fetch all the rows in a list of lists.
	   results = cursor.fetchall()
	   print>>output, "Current 2:"
	   for row in results:
	     s_id = row[0]
	     s_type = row[1]
	     data = row[2]
	     timestamp = row[3]
	     # Now print fetched result
	     print>>output, "%s, %s, %s, %s" % \
		    (s_id, s_type, data, timestamp)

	   print>>output, ""

	except:
	   print "Error: unable to fetch data"

	# Check the strategy commands in the database
	sql = "SELECT * FROM GPS"

	try:
	   # Execute the SQL command
	   cursor.execute(sql)
	   # Fetch all the rows in a list of lists.
	   results = cursor.fetchall()
	   print>>output, "GPS:"
	   for row in results:
	     s_id = row[0]
	     longtitude = row[1]
	     lattitude = row[2]
	     speed = row[3]
	     timestamp = row[4]
	     # Now print fetched result
	     print>>output, "%s, %s, %s, %s, %s" % \
		    (s_id, longtitude, lattitude, speed, timestamp)

	   print>>output, ""

	except:
	   print "Error: unable to fetch data"

	# disconnect from server
	print "\nDatabase written to file: " + name
	db.close()
