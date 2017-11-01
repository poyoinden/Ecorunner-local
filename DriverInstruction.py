from Instruction import Instruction

""" Class for the driver instruction object """
class DriverInstruction(Instruction):

	def __init__(self, throttle, displaySwitch, timestamp):
		Instruction.__init__(self, "Driver", timestamp)
		self.throttle = throttle
		self.displaySwitch = displaySwitch

	def getThrottle(self):
		return self.throttle

	def getDisplaySwitch(self):
		return self.displaySwitch

	def toString(self):
		return "type: " + self.getType() + ", throttle: " + str(self.throttle) + ", displaySwitch: " + str(self.displaySwitch) + ", timestamp: " + str(self.timestamp)
