""" Class for the abstract object instruction """
class Instruction(object):
	def __init__(self, insType, timestamp):
		self.insType = insType
		self.timestamp = timestamp

	def getType(self):
		return self.insType

	def getTimestamp(self):
		return self.timestamp
