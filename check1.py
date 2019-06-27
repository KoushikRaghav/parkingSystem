numb = 0
vehData = []
parkingData = []
dictData = []
floorList = []
vehicleType = 0
numOfFloors = 2
vehicleData = []
vehicleNumber = []	
floorData = []
vehicleList = ["Car","Bike"]

class Parking:
	def __init__(self,vehicleData,total):
		self.vehicleData = vehicleData
		self.total = total

	def getDict(self):
		return self.vehicleData

class Floor():
	def __init__(self,floor):
		self.floor = floor		

	def getFloorNum(self):
		return self.floor

class Vehicle:
	def __init__(self,vType,vNumber):
		self.VType = vType
		self.VNumber = vNumber

	def getVType(self):
		return self.VType

	def getNumber(self):
		return self.VNumber

def unparkVehicle():
	print "\n<--- VEHICLE UNPARKING --->"
	getVehNum = int(input("\nEnter your vehicle number: "))
	if getVehNum in vehicleNumber:
		print "\nYour vehicle is found"
		for unPark in vehData:
			print "\n\tFloor: {}".format(unPark.getFloorNum())
			print "\n\tVehicle Type: {}".format(vehicleList[vehicleData.getVType()])
			print "\n\tVehicle Number: {}".format(vehicleData.getNumber())
			print "\n\t!!! UNPARKED !!!"
		# 	if unPark.getVTtype() == 0:
		# 		floorList.car += 1
		# 	elif unPark.getVTtype() == 1:
		# 		floorList.bike += 1
		# 	elif unPark.getVTtype() == 2:
		# 		floorList.bus += 1
		# 	elif unPark.getVTtype() == 3:
		# 		floorList.van += 1		
	else:
		print "\nYour vehicle is not found"

def parkVehicle(floor):
	global floorList,floorData,vehData
	floorList = parkingData.getDict()[floor][vehicleList[vehicleType]]
	floorData = Floor(floor)
	vehData.append(floorData)
	if vehicleData.getVType() < len(vehicleList):
		print "\n  !! Your {} is parked !!".format(vehicleList[vehicleType])
		print "\n\t{} Number: {}".format(vehicleList[vehicleType],vehicleData.getNumber())
		# import pdb; pdb.set_trace()
		print "\n\tFloor: {}".format(floorData.getFloorNum())
		if floorList != 0:
			floorList -= 1
			print "\n\t!!! PARKED !!!"
			print "{}".format(floorList)

def searchFloors():
	if vehicleType < len(vehicleList):	
		print "\nYour vehicle is {}\n".format(vehicleList[vehicleType])
		for i in range(len(vehicleList)):
			# import pdb; pdb.set_trace()
			# if parking.getFloorNum(i).isVehicleAvailable(vehicleData.getVType()):

			if parkingData.getDict()[i][vehicleList[vehicleData.getVType()]] > 0:		
				print "Floor {} --> AVAILABLE\n\t".format(i) 
			else:
			 	print "\t"
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
	print "\n<--- VEHICLE PARKING --->"
	print "\nEnter Vehicle Type:\n"
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
	global numOfFloors,dictData,parkingData
	print "\n<--- ENTER VEHICLE DATA --->"
	for numOfFloors in range(2):
		vehicleDict = {}
		print "\n    --- Floor {} ---".format(numOfFloors)
		vehicleLimit = int(input("\nEnter the number of vehicles: "))
		totalvehicles = 0
		for vehicles in vehicleList:
			vehicleDict[vehicles] = int(input("\n\t {}: ".format(vehicles)))
			totalvehicles += vehicleDict[vehicles]
		dictData.append(vehicleDict)		
		if totalvehicles == vehicleLimit:
			parkingData = Parking(dictData,totalvehicles)
			print "\n",parkingData.getDict()
			print "\nDATA STORED SUCCESSFULLY"
		else:
			print "\nEnter vehicles count within {}\n".format(vehicleLimit)
			break
		
def getMenuOption():
	option = int(input("1. Enter Data\n2. Park my vehicle\n3. Unpark my vehicle\n4. Display Availability\n5. Exit\n\n"))
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
		elif option == 4:
			displayVehicleData()
		elif option >= 5 or option == 0:
			print "BYE"
			exit()
	
if __name__ == '__main__':						
	main()