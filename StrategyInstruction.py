from Instruction import Instruction

""" Class for the strategy instruction object """
class StrategyInstruction(Instruction):
	def __init__(self, fcPower, throttleAdv, motorSet, timestamp):
		Instruction.__init__(self, "Strategy", timestamp)
		self.fcPower = fcPower
		self.throttleAdv = throttleAdv
		self.motorSet = motorSet

	def getFcPower(self):
		return self.fcPower

	def getThrottleAdv(self):
		return self.throttleAdv

	def getMotorSet(self):
		return self.motorSet

	def getTimestamp(self):
		return self.timestamp

	def toString(self):
		return "type: " + self.getType() + ", fc Power: " + str(self.fcPower) + ", throttle advice: " + str(self.throttleAdv) + ", motor settings: " + str(self.motorSet) + ", timestamp: " + str(self.timestamp)
