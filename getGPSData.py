import sys
import time
import pynmea2
import re
from GPS import GPS

def getGPSData(tn):
	while True:
		incoming = tn.read_until("\n")
		splitup = re.split(',', incoming)

		try:
			if splitup[0] == "$GPRMC":	
				msg = pynmea2.parse(incoming)
				lon = str(msg.lon) 
				lat = str(msg.lat)
				gps = GPS(lon, lat, msg.spd_over_grnd, msg.timestamp)
				return gps
				break
		
		except AttributeError:
			pass
	
		except:	
			print "unknown exception found in getGPSData.py"	



	
