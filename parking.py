class Parking:
	def __init__(self,car,bike,bus,van):
		self.car = car
		self.bike = bike
		self.bus = bus
		self.van = van

	def getTotalVehicles(self):
		return self.car+self.bike+self.bus+self.van

