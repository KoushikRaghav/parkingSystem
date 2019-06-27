numb = 0
parking = []
floorList = []
vehicleType = 0
numOfFloors = 2
parkingData = []
vehicleData = []
vehicleNumber = []	
vehicleList = ["Car","Bike"]

class Floor:
	def __init__(self,floordata):
		self.floordata = floordata

	def setFloorData(self,Floordata):
		self.floordata = Floordata
	
	def getFloorData(self):
		return self.floordata

	def isVehicleAvailable(self,vehicleName):
		return True if self.floordata[vehicleName] > 0 else False	
		
class Parking:
	def __init__(self,allData):
		self.allData = allData

	def getAllData(self):
		return self.allData

class Vehicle:
	def __init__(self,vType,vNumber):
		self.VType = vType
		self.VNumber = vNumber

	def getVType(self):
		return self.VType

	def getNumber(self):
		return self.VNumber

def parkVehicle(floor):
	print "\n  !! Your {} is parked !!".format(vehicleList[vehicleType])
	print "\n\t{} Number: {}".format(vehicleList[vehicleType],vehicleData.getNumber())
	print "\n\tFloor: {}".format(floor)	
	parkingData.getAllData()[floor][vehicleList[vehicleType]] -= 1
	print "\n\t!!! PARKED !!!", parkingData.getAllData()[floor][vehicleList[vehicleType]]
	
def searchFloors():
	if vehicleType < len(vehicleList):	
		print "\nYour vehicle is {}\n".format(vehicleList[vehicleType])
		for i in range(len(vehicleList)):
			floorData.setFloorData(parkingData.getAllData()[i])
			print "Floor {} --> AVAILABLE\n\t".format(i) if floorData.isVehicleAvailable(vehicleList[vehicleData.getVType()]) == True else "\t"	
		floor = int(input("Enter the floorNum: "))
		return floor

def checkForAvailability():
	return True if vehicleType < len(vehicleList) else False

def checkVehicleNumber(numb):
	count = 0
	while numb > 0:
		numb = numb // 10
    	count += 1
	return True if count == 4 else False

def getVehicleData():
	global numb,vehicleType,vehicleData
	print "\n<--- VEHICLE PARKING --->\n\nEnter Vehicle Type:\n"
	for vehicles in vehicleList:
		print "{}. {}".format(vehicleList.index(vehicles),vehicles)
	vehicleType = int(input("\n"))
	if vehicleType < len(vehicleList):
		numb = int(input("\n\nEnter Vehicle Number: "))
		vehicleData = Vehicle(vehicleType,numb)
		print vehicleData.getVType(),vehicleData.getNumber()
		return 1 if checkVehicleNumber(numb) == True  else 0	
	else:
		print "Enter the vehicle type correctly"

def enterVehicleData():
	global numOfFloors,parkingData,floorData,parking
	print "\n<--- ENTER VEHICLE DATA --->"
	for numOfFloors in range(2):
		vehicleDict = {}
		print "\n    --- Floor {} ---".format(numOfFloors)
		vehicleLimit = int(input("\nEnter the number of vehicles: "))
		totalvehicles = 0
		for vehicles in vehicleList:
			vehicleDict[vehicles] = int(input("\n\t {}: ".format(vehicles)))
			totalvehicles += vehicleDict[vehicles]		
		if totalvehicles == vehicleLimit:
			floorData = Floor(vehicleDict)
			print "\n",floorData.getFloorData()
			parking.append(vehicleDict)
			parkingData = Parking(parking)
			print "\n",parkingData.getAllData()
			print "\nDATA STORED SUCCESSFULLY"
		else:
			print "\nEnter vehicles count within {}\n".format(vehicleLimit)
			break
		
def getMenuOption():
	option = int(input("1. Enter Data\n2. Park my vehicle\n3. Unpark my vehicle\n4. Exit\n\n"))
	return option

def main():
	global vehicleNumber,numOfFloors
	while 1:
		print "\n<--- PARKING SYSTEM --->\n"
		option = getMenuOption()
		if option == 1:
			enterVehicleData()		
		elif option == 2:
			VData = getVehicleData()
			vehicleNumber.append(numb)		
			check = checkForAvailability()
			floor = searchFloors() if check == True else "\nEnter Correct Vehicle Type\n"
			parkVehicle(floor) if floor <= numOfFloors else "\nPARKING IS FULL IN FLOOR {}".format(floor)
		elif option == 3:
			unparkVehicle()
		elif option >= 4 or option == 0:
			print "BYE"
			exit()
	
if __name__ == '__main__':						
	main()