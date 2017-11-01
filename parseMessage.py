from Instruction import Instruction
from GBInstruction import GBInstruction
from DriverInstruction import DriverInstruction
from StrategyInstruction import StrategyInstruction
from SensorData import SensorData
import re

""" Method for parsing incoming strings called messages """
def parseMessage(inputString):
	# Split the string in parts into a list
	splitUp = re.split(',', inputString)
	length = len(splitUp)

	# Create a gb instruction object from the message 
	if splitUp[0] == 'gb' and length == 6:
		try:
			g = GBInstruction(splitUp[1], splitUp[2], splitUp[3], splitUp[4], splitUp[5])
			return g	


		except IndexError:
			print "Invalid GB instruction format, instruction not created"

	else:
		print "Incorrect parser format"
