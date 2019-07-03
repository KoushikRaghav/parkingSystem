from floor import Floor

class Parking:
	def __init__(self):
		self.data = []
		
	def addFloorData(self,floor):
		self.data.append(floor)

	def getData(self,i):
		return self.data[i]

	def getParkingData(self,vehicleList):
		print "\n<--- ENTER VEHICLE DATA --->"
		for numOfFloors in range(2):
			vehicleDict = {}
			print "\n    --- Floor {} ---".format(numOfFloors)
			vehicleLimit = int(input("\nEnter the Number of vehicles: "))
			totalvehicles = 0
			for vehicles in vehicleList:
				vehicleDict[vehicles] = int(input("\n\t {}: ".format(vehicles)))
				totalvehicles += vehicleDict[vehicles]		
			if totalvehicles == vehicleLimit:
				self.floorObject = Floor(vehicleDict)
				print "\nDATA STORED SUCCESSFULLY"
			else:
				print "\nEnter vehicles count within {}\n".format(vehicleLimit)
				break
			self.addFloorData(self.floorObject)
		return self.data,self.floorObject

	def displayParkingData(self):
		for vehicles in range(len(self.data)):	
			print "\n {}\t{} ".format(vehicles,str(self.data[vehicles].getData()))

	def listAvailableFloors(self,vehicleType,vehicleData,vehicleList):
		for i in range(2):
			if self.data[i].isVehicleAvailable(vehicleList[vehicleType]) == True:
				print "Floor {} --> AVAILABLE\n\t".format(i)  
			else:
				print "\t"	
	