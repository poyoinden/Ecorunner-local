from parseMessage import parseMessage
from writeMessage import writeMessage
from GPS import GPS
from SensorData import SensorData
import boto.sqs
from boto.sqs.message import Message
import time


def makeMessage(ObjectToSend, queue):
		if isinstance(ObjectToSend, GPS):
			m = Message()
			m.set_body(writeMessage(ObjectToSend))
			queue.write(m)
			print "Sent GPS data to ground base"			

		elif isinstance(ObjectToSend, SensorData):
			m = Message()
			m.set_body(writeMessage(ObjectToSend))
			queue.write(m)
			print "Sent " + str(ObjectToSend.getMsgType()) + " data to ground base"

		else:
			print "Wrong message type, nothing sent"
			time.sleep(5)
		
