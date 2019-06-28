class Parking:
	def __init__(self):
		self.data = []
	
	def addFloorData(self, floors):
		self.data.append(floors)
	
	def getAllData(self):
		return self.data