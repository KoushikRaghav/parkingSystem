vehicleList = ["Car","Bike"]
vehicleType = 0

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

class Parking:
	def __init__(self):
		self.data = []
	
	def addFloorData(self, floors):
		self.data.append(floors)
	
	def getAllData(self):
		return self.data

class Vehicle:
	def __init__(self,vType,VNumber):
		self.VType = vType
		self.Vnumber = VNumber

	def getVType(self):
		return self.VType

	def getnumber(self):
		return self.Vnumber

def unparkVehicle(vehicledata):
	park = parkingData.getAllData()
	print "\n<--- VEHICLE UNPARKING --->"
	getVehNum = int(input("\nEnter your vehicle Number: "))
	for floors in park:
		for vehicles in floors.showVehicles():
			if vehicles.getnumber() == getVehNum:
				print "\nYour vehicle is found in floor: {}".format(park.index(floors))
  				print "\n\tVehicle Type: {}".format(vehicles.getVType())
				print "\n\tVehicle Number: {}".format(vehicles.getnumber())
				print "\n\t!!! UNPARKED !!!"
				park[park.index(floors)].getFloorData()[vehicleList[vehicles.getVType()]]+= 1
				print park[park.index(floors)].getFloorData()[vehicleList[vehicles.getVType()]]

def parkVehicle(floorNum,vehicleData):
	park = parkingData.getAllData() 
	print "\n  !! Your {} is parked !!".format(vehicleList[vehicleType])
	print "\n\t{} Number: {}".format(vehicleList[vehicleType],vehicleData.getnumber())
	print "\n\tFloor: {}".format(floorNum)	
	park[floorNum].getFloorData()[vehicleList[vehicleType]] -= 1
	print "\n\t!!! PARKED !!!", park[floorNum].getFloorData()[vehicleList[vehicleType]]

def searchForAvailableFloors(number):
	print "\nYour vehicle is {}\n".format(vehicleList[vehicleType])
	for i in range(2):
		if  parkingData.getAllData()[i].isVehicleAvailable(vehicleList[vehicleType]) == True:
			print "Floor {} --> AVAILABLE\n\t".format(i)  
		else:
			print "\t"	
	floorNum = int(input("Enter the floorNum: "))
	parkingData.getAllData()[floorNum].addVehicles(Vehicle(vehicleType,number))
	return floorNum

def getVehicleData():	
	print "\n<--- VEHICLE PARKING --->\n\nEnter Vehicle Type:\n"
	for vehicles in vehicleList:
		print "{}. {}".format(vehicleList.index(vehicles),vehicles)
	vehicleType = int(input("\n"))
	if vehicleType < len(vehicleList):
		number = int(input("\n\nEnter Vehicle Number: "))	
		vehicleData = Vehicle(vehicleType,number)
		return vehicleData,number
	else:
		print "Enter the vehicle type correctly"

def displayVehicleData():
	for vehicles in range(len(parkingData.getAllData())):	
		print "\n {}\t{} ".format(vehicles,str(parkingData.getAllData()[vehicles].getFloorData()).replace("{","").replace("}", ""))

def enterVehicleData():
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
			enterVehicleData()		
		elif option == 2:
			vehicledata,number = getVehicleData()	
			floorNum = searchForAvailableFloors(number) 
			parkVehicle(floorNum,vehicledata) if floorNum <= numOfFloors else "\nPARKING IS FULL IN FLOOR {}".format(floorNum)
		elif option == 3:
			unparkVehicle(vehicledata)
		elif option == 4:
			displayVehicleData()
		elif option >= 5 or option == 0:
			print "BYE"
			exit()
	
if __name__ == '__main__':						
	main()