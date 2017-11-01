from Instruction import Instruction

""" Class for the gb instruction object """
class GBInstruction(Instruction):

	def __init__(self, fcPower, throttleAdv, steerAdv, motorSet, timestamp):
		Instruction.__init__(self, "GB", timestamp)
		self.fcPower = fcPower
		self.throttleAdv = throttleAdv
		self.steerAdv = steerAdv
		self.motorSet = motorSet

	def getFcPower(self):
		return self.fcPower

	def getThrottleAdv(self):
		return self.throttleAdv

	def getSteerAdv(self):
		return self.steerAdv

	def getMotorSet(self):
		return self.motorSet

	def toString(self):
		return "type: " + self.getType()  + ", fc Power: " + str(self.fcPower) + ", throttle advice: " + str(self.throttleAdv) + ", Steer advice: " + str(self.steerAdv) + ", motor settings: " + str(self.motorSet) + ", timestamp: " + str(self.timestamp)
