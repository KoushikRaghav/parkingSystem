vehList = []
floorData = []
vehicleType = 0
numOfFloors = 2
parkingData = []
vehicleNumberList = []	
floorList = []
vehicleList = ["Car","Bike"]

class Floor:
	def __init__(self,floordata):
		self.floordata = floordata
		
	def getFloorData(self):
		return self.floordata

	def isVehicleAvailable(self,vehicleName):
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
	import pdb;pdb;pdb.set_trace()
	print "\n<--- VEHICLE UNPARKING --->"
	getVehNum = int(input("\nEnter your vehicle Number: "))
	for i in range(len(vehList)):
		if vehList[i].getnumber() == getVehNum:
			print i
		# if vehicledata.getnumber() == getVehNum:
		# 	print "\nYour vehicle is found in floor: {}".format()
		# 	print "\n\tVehicle Type: {}".format(vehicleList[vehList[i].getVType()])
		# 	print "\n\tVehicle Number: {}".format(vehList[i].getnumber())
		# 	print "\n\t!!! UNPARKED !!!"
		# if floorList[i][i].getnumber() == getVehNum:
		# 	print "\nYour vehicle is found in floor: {}".format(floorList[i].index(floorList[i][i]))
		# 	print "\n\tVehicle Type: {}".format(vehicleList[vehList[i].getVType()])
		# 	print "\n\tVehicle Number: {}".format(vehList[i].getnumber())
		# 	print "\n\t!!! UNPARKED !!!"
		# else:
		# 	print "no"
		# if vehicleNumberList[i] == getVehNum:



	# for i in range(len(vehicleNumberList)):
	# 	if vehicleNumberList[i] == getVehNum:
	# 		import pdb; pdb.set_trace()
	# 		print "\nYour vehicle is found in floor: {}".format(vehList[i].setFloor())
	# 		print "\n\tVehicle Type: {}".format(vehicleList[vehList[i].getVType()])
	# 		print "\n\tVehicle Number: {}".format(vehList[i].getnumber())
	# 		print "\n\t!!! UNPARKED !!!"
	# 		floorData[vehList[i].getFloor()].getFloorData()[vehicleList[vehicleData.getVType()]] += 1
	# 		print floorData[vehList[i].getFloor()].getFloorData()[vehicleList[vehicleData.getVType()]] 
	
def parkVehicle(floorNum,vehicleData):
	# import pdb;pdb;pdb.set_trace()
	print "\n  !! Your {} is parked !!".format(vehicleList[vehicleType])
	print "\n\t{} Number: {}".format(vehicleList[vehicleType],vehicleData.getnumber())
	print "\n\tFloor: {}".format(floorNum)	
	floorData[floorNum].getFloorData()[vehicleList[vehicleType]] -= 1
	print "\n\t!!! PARKED !!!", floorData[floorNum].getFloorData()[vehicleList[vehicleType]]
	
def searchForAvailableFloors():
	print "\nYour vehicle is {}\n".format(vehicleList[vehicleType])
	for i in range(2):
		if floorData[i].isVehicleAvailable(vehicleList[vehicleType]) == True:
			print "Floor {} --> AVAILABLE\n\t".format(i)  
		else:
			print "\t"	
	floorNum = int(input("Enter the floorNum: "))
	return floorNum

def getVehicleData():
	global vehicleType,vehList,floorList
	print "\n<--- VEHICLE PARKING --->\n\nEnter Vehicle Type:\n"
	for vehicles in vehicleList:
		print "{}. {}".format(vehicleList.index(vehicles),vehicles)
	vehicleType = int(input("\n"))
	if vehicleType < len(vehicleList):
		number = int(input("\n\nEnter Vehicle Number: "))
		vehicleNumberList.append(number)	
		vehicleData = Vehicle(vehicleType,number)
		vehList.append(vehicleData)
		# import pdb; pdb.set_trace()
		# floorList.append(vehList)
		return vehicleData
	else:
		print "Enter the vehicle type correctly"

def displayVehicleData():
	# print "_-"*23
	# print "\nData\t\tTotal"
	# print "_-"*23
	# import pdb; pdb.set_trace()
	for vehicles in range(len(vehicleList)):
		print "\n ",parkingData.getAllData()[vehicles].getFloorData()

def enterVehicleData():
	global numOfFloors,floorData,parkingData
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
			floorData.append(floorObject)
			print "\nDATA STORED SUCCESSFULLY"
		else:
			print "\nEnter vehicles count within {}\n".format(vehicleLimit)
			break
		parkingData.addFloorData(floorObject)

def getMenuOption():
	option = int(input("1. Enter Data\n2. Park my vehicle\n3. Unpark my vehicle\n4. Display Data\n5. Exit\n\n"))
	return option

def main():
	global vehicleNumberList,numOfFloors
	while 1:
		print "\n<--- PARKING SYSTEM --->\n"
		option = getMenuOption()
		if option == 1:
			enterVehicleData()		
		elif option == 2:
			vehicledata = getVehicleData()	
			floorNum = searchForAvailableFloors() 
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