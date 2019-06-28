class Floor:
	def __init__(self, floordata):
		self.floordata = floordata
		self.vehicles = []
	
	def addVehicles(self, vehicless):
		self.vehicles.append(vehicless)

	def showVehicles(self):
		return self.vehicles

	def getFloorData(self):
		return self.floordata

	def isVehicleAvailable(self, vehicleName):
		return True if self.floordata[vehicleName] > 0 else False	
