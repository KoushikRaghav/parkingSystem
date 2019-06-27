class Vehicle:
	def __init__(self,vType,vNumber,floor):
		self.VType = vType
		self.VNumber = vNumber
		self.VFloor = floor

	def getFloor(self):
		return self.VFloor

	def getVTtype(self):
		return self.VType

	def getNumber(self):
		return self.VNumber