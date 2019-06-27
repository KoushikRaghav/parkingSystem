numb = 0
vehData = []
parkingData = []
floorList = []
vehicleType = 0
numOfFloors = 2
vehicleData = []
vehicleNumber = []	
floorData = []
vehicleList = ["Car","Bike"]

class Floor:
	def __init__(self,floor,data):
		self.floor = floor
		self.data = data

	def getDict(self):
		return self.data

	def setFloor(self,i):	
		self.floor = i
		# print i
		
	def isVehicleAvailable(self,name):
		# import pdb;pdb.set_trace()
		self.name = name
		if self.data[self.floor][self.name]>0:
			return True
		else:
			return False

class Vehicle:
	def __init__(self,vType,vNumber):
		self.VType = vType
		self.VNumber = vNumber

	def getVType(self):
		return self.VType

	def getNumber(self):
		return self.vNumber

def searchFloors():
	if vehicleType < len(vehicleList):	
		print "\nYour vehicle is {}\n".format(vehicleList[vehicleType])
		for i in range(len(vehicleList)):
			floorData.setFloor(i)
			if floorData.isVehicleAvailable(vehicleList[vehicleData.getVType()]) == True:
				print "haloooo bosss"
			else:
				print "Sorry bosss"
			# import pdb;pdb.set_trace()
			# floorData.setFloor(i)
			# if floorData.setFloor(i).isVehicleAvailable(vehicleData.getVType()) == True:
			# 	print "yes"
			# else:
			# 	print "no"
			# if parking.getFloorNum(i).isVehicleAvailable(vehicleData.getVType()): -->venkat
		# 	if parkingData.getDict()[i][vehicleList[vehicleData.getVType()]] > 0:		
		# 		print "Floor {} --> AVAILABLE\n\t".format(i) 
		# 	else:
		# 	 	print "\t"
		# floor = int(input("Enter the floorNum: "))
		# return floor

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
	global numOfFloors,dictData,parkingData,floorData
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
			floorData = Floor(numOfFloors,vehicleDict)
			print "\n",floorData.getDict()
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