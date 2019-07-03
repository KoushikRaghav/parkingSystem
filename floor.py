class Floor:
	def __init__(self, floordata):
		self.floordata = floordata
		self.vehicles = []
	
	def addVehicle(self, vehicle):
		self.vehicles.append(vehicle)

	def getVehicle(self):
		return self.vehicles

	def setParkingData(self,i):
		self.floordata[i] -= 1

	def setUnParkData(self,i):
		self.floordata[i] += 1

	def getData(self):
		return self.floordata

	def getFloorData(self,i):
		return self.floordata[i]

	def isVehicleAvailable(self, vehicleName):
		return True if self.floordata[vehicleName] > 0 else False	

	def parkVehicle(self,parkingData,vehicleData,vehicleList):
		floorNum = int(input("Enter the floorNum: "))
		parkingData[floorNum].addVehicle(vehicleData)
		print "\n  !! Your {} is parked !!".format(vehicleList[vehicleData.getVType()])
		print "\n\t{} Number: {}".format(vehicleList[vehicleData.getVType()],vehicleData.getNumber())
		print "\n\tFloor: {}".format(floorNum)
		parkingData[floorNum].setParkingData(vehicleList[vehicleData.getVType()])
		print "\n\t!!! PARKED !!!", parkingData[floorNum].getFloorData(vehicleList[vehicleData.getVType()])

	def unparkVehicle(self,floors,vehicleList):
		print "\n<--- VEHICLE UNPARKING --->"
		getVehNum = int(input("\nEnter your vehicle Number: "))
		for floor in floors:
			floorid = floors.index(floor)
			for vehicles in floor.getVehicle():
				if vehicles.getNumber() == getVehNum:		
					print "\nYour vehicle is found in floor: {}".format(floorid)
	  				print "\n\tVehicle Type: {}".format(vehicles.getVType())
					print "\n\tVehicle Number: {}".format(vehicles.getNumber())
					print "\n\t!!! UNPARKED !!!"
					floors[floors.index(floor)].setUnParkData(vehicleList[vehicles.getVType()])
					print floors[floors.index(floor)].getFloorData(vehicleList[vehicles.getVType()])
					del floors[floorid].getVehicle()[floor.getVehicle().index(vehicles)]

	