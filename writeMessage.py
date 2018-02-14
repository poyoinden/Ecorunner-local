import boto.sqs
from boto.sqs.message import Message
from SensorData import SensorData
from GPS import GPS

""" Write a message from Ecorunner to ground base """
def writeMessage(objectToSend):
	# Write the message for sensor data
	if isinstance(objectToSend, SensorData):
		mString = "se," + str(objectToSend.getSensorId()) + "," + str(objectToSend.getMsgType()) + "," + str(objectToSend.getData()) + "," + str(objectToSend.getTimestamp())
		return mString	

	# Write the message for gps data
	elif isinstance(objectToSend, GPS):
		mString = "gp," + str(objectToSend.getLongtitude()) + "," + str(objectToSend.getLattitude()) + "," + str(objectToSend.getSpeed()) + "," + str(objectToSend.getTimestamp())
		return mString

	# If for some reason an incorrect object is passed, do nothing
	else:
		pass
