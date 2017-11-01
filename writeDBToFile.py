import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","reverse","mydata" )
cursor = db.cursor()

# Check the driver commands in the database
sql = "SELECT * FROM DriverInstructions"

try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   print "Driver instructions:"
   for row in results:
      i_id = row[0]
      throttle = row[1]
      displayswitch = row[2]
      timestamp = row[3]
      # Now print fetched result
      print "id=%s,throttle=%s, displayswitch=%s, timestamp=%s" % \
             (i_id, throttle, displayswitch, timestamp)

   print "----------------"

except:
   print "Error: unable to fetch data"

# Check the GB commands in the database
sql = "SELECT * FROM GBInstructions"

try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   print "GB instructions:"
   for row in results:
      i_id = row[0]
      fcpower = row[1]
      throttleadv = row[2]
      steeradv = row[3]
      motorset = row[4]
      timestamp = row[5]
      # Now print fetched result
      print "id=%s,fcpower=%s, throttleadvice=%s, steeradvice=%s, motorsettings=%s, timestamp=%s" % \
             (i_id, fcpower, throttleadv, steeradv, motorset, timestamp)

   print "----------------"

except:
   print "Error: unable to fetch data"


# Check the strategy commands in the database
sql = "SELECT * FROM StrategyInstructions"

try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   print "Strategy instructions:"
   for row in results:
     i_id = row[0]
     fcpower = row[1]
     throttleadv = row[2]
     motorset = row[3]
     timestamp = row[4]
     # Now print fetched result
     print "id=%s,fcpower=%s, throttleadvice=%s, motorsettings=%s, timestamp=%s" % \
            (i_id, fcpower, throttleadv, motorset, timestamp)

   print "----------------"

except:
   print "Error: unable to fetch data"

# Check the strategy commands in the database
sql = "SELECT * FROM SensorData"

try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   print "Sensor data:"
   for row in results:
     s_id = row[0]
     s_type = row[1]
     data = row[2]
     timestamp = row[3]
     # Now print fetched result
     print "id=%s,type=%s, data=%s, timestamp=%s" % \
            (s_id, s_type, data, timestamp)

   print "----------------"

except:
   print "Error: unable to fetch data"

# disconnect from server
db.close()
