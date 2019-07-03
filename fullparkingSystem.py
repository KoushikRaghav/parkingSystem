class Parking:
	def __init__(self):
		self.data = []
	
	def addFloorData(self, floors):
		self.data.append(floors)

	def getAllData(self):
		return self.data

	def getData(self,i):
		return self.data[i]

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

	def getFloorData(self,i):
		return self.floordata[i]

	def isVehicleAvailable(self, vehicleName):
		return True if self.floordata[vehicleName] > 0 else False	

class Vehicle:
	def __init__(self,vType,VNumber):
		self.VType = vType
		self.Vnumber = VNumber

	def getVType(self):
		return self.VType

	def getNumber(self):
		return self.Vnumber

vehicleList = ["Car","Bike"]
vehicleType = 0

def unparkVehicle(floors):
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

def parkVehicle(floors,vehicleData):
	floorNum = int(input("Enter the floorNum: "))
	parkingData.getData(floorNum).addVehicle(vehicledata)
	print "\n  !! Your {} is parked !!".format(vehicleList[vehicleType])
	print "\n\t{} Number: {}".format(vehicleList[vehicleType],vehicleData.getNumber())
	print "\n\tFloor: {}".format(floorNum)
	floors[floorNum].setParkingData(vehicleList[vehicleData.getVType()])
	print "\n\t!!! PARKED !!!", floors[floorNum].getFloorData(vehicleList[vehicleData.getVType()])

def listAvailableFloors():
	print "\nYour vehicle is {}\n".format(vehicleList[vehicleType])
	for i in range(2):
		if parkingData.getData(i).isVehicleAvailable(vehicleList[vehicleType]) == True:
			print "Floor {} --> AVAILABLE\n\t".format(i)  
		else:
			print "\t"	
	
def getVehicleData():	
	print "\n<--- VEHICLE PARKING --->\n\nEnter Vehicle Type:\n"
	for vehicles in vehicleList:
		print "{}. {}".format(vehicleList.index(vehicles),vehicles)
	vehicleType = int(input("\n"))
	if vehicleType < len(vehicleList):
		number = int(input("\n\nEnter Vehicle Number: "))	
		vehicleData = Vehicle(vehicleType,number)
		return vehicleData
	else:
		print "Enter the vehicle type correctly"

def displayParkingData(floors):
	for vehicles in range(len(floors)):	
		print "\n {}\t{} ".format(vehicles,str(parkingData.getData(vehicles).getFloorData()).replace("{","").replace("}", ""))

def enterParkingData():
	global parkingData
	print "\n<--- ENTER VEHICLE DATA --->"
	parkingData = Parking()
	for numOfFloors in range(2):
		vehicleDict = {}
		print "\n    --- Floor {} ---".format(numOfFloors)
		vehicleLimit = int(input("\nEnter the Number of vehicles: "))
		totalvehicles = 0
		for vehicles in vehicleList:
			vehicleDict[vehicles] = int(input("\n\t {}: ".format(vehicles)))
			totalvehicles += vehicleDict[vehicles]		
		if totalvehicles == vehicleLimit:
			floorObject = Floor(vehicleDict)
			print "\nDATA STORED SUCCESSFULLY"
		else:
			print "\nEnter vehicles count within {}\n".format(vehicleLimit)
			break
		parkingData.addFloorData(floorObject)

def getMenuOption():
	option = int(input("1. Enter Data\n2. Park my vehicle\n3. Unpark my vehicle\n4. Display Data\n5. Exit\n\n"))
	return option

def main():
	numOfFloors = 2	
	while 1:
		print "\n<--- PARKING SYSTEM --->\n"
		option = getMenuOption()
		if option == 1:
			enterParkingData()		
		elif option == 2:
			vehicledata = getVehicleData()	
			listAvailableFloors() 
			floors = parkingData.getAllData()
			parkVehicle(floors,vehicledata) if floorNum <= numOfFloors else "\nPARKING IS FULL IN FLOOR {}".format(floorNum)
		elif option == 3:
			unparkVehicle(floors)
		elif option == 4:
			displayParkingData(floors)
		elif option >= 5 or option == 0:
			print "BYE"
			exit()
	
if __name__ == '__main__':						
	main()