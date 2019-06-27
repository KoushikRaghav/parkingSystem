from parking import Parking
from vehicle import Vehicle

vehicleData = []
floorList = []
numb = 0
vehData = []
vehicleType = 0
numOfFloors = 3
parkingData = []
vehicleNumber = []
vehicleList = ["Car","Bike","Bus","Van"]

def updateData():
	for unPark in vehData:
		if unPark.getVTtype() == 0:
			floorList.car += 1
		elif unPark.getVTtype() == 1:
			floorList.bike += 1
		elif unPark.getVTtype() == 2:
			floorList.bus += 1
		elif unPark.getVTtype() == 3:
			floorList.van += 1

def unparkVehicle():
	print "\n<--- VEHICLE UNPARKING --->"
	getVehNum = int(input("\nEnter your vehicle number: "))
	if getVehNum in vehicleNumber:
		print "\nYour vehicle is found"
		for unPark in vehData:
			import pdb; pdb.set_trace()
			print "\n\tFloor: {}".format(unPark.getFloor())
			print "\n\tVehicle Type: {}".format(vehicleList[unPark.getVTtype()])
			print "\n\tVehicle Number: {}".format(unPark.getNumber())
			print "\n\t!!! UNPARKED !!!"		
	else:
	 	print "\nYour vehicle is not found"
	
def parkVehicle(floor):
	global floorList,vehicleData,vehData
	floorList = parkingData[floor]
	vehicleData = Vehicle(vehicleType,numb,floor)
	vehData.append(vehicleData)
	if vehicleType == 0:
		print "\n  !! Your {} is parked !!".format(vehicleList[vehicleType])
		print "\n\t{} Number: {}".format(vehicleList[vehicleType],vehicleData.getNumber())
		print "\n\tFloor: {}".format(vehicleData.getFloor())
		if floorList.car != 0:
			floorList.car -= 1
			print "\n\t!!! PARKED !!!"
			print "{}".format(floorList.car)
			print "{}".format(floorList.getTotalVehicles())
		else:
			print "\nPARKING FULL\n"
	elif vehicleType == 1:
		print "\n  !! Your {} is parked !!".format(vehicleList[vehicleType])
		print "\n\t{} Number: {}".format(vehicleList[vehicleType],vehicleData.getNumber())
		print "\n\tFloor: {}".format(vehicleData.getFloor())
		if floorList.bike != 0:
			floorList.bike -= 1
			print "\n\t!!! PARKED !!!"
			print "{}".format(floorList.bike)
			print "{}".format(floorList.getTotalVehicles())
		else:
			print "\nPARKING FULL\n"
	elif vehicleType == 2:
		print "\n  !! Your {} is parked !!".format(vehicleList[vehicleType])
		print "\n\t{} Number: {}".format(vehicleList[vehicleType],vehicleData.getNumber())
		print "\n\tFloor: {}".format(vehicleData.getFloor())
		if floorList.bus != 0:
			floorList.bus -= 1
			print "\n\t!!! PARKED !!!"
			print "{}".format(floorList.bus)
			print "{}".format(floorList.getTotalVehicles())
		else:
			print "\nPARKING FULL\n"
	elif vehicleType == 3:
		print "\n  !! Your {} is parked !!".format(vehicleList[vehicleType])
		print "\n\t{} Number: {}".format(vehicleList[vehicleType],vehicleData.getNumber())
		print "\n\tFloor: {}".format(vehicleData.getFloor())	
		if floorList.van != 0:
			floorList.van -= 1
			print "\n\t!!! PARKED !!!"
			print "{}".format(floorList.van)
			print "{}".format(floorList.getTotalVehicles())
		else:
			print "\nPARKING FULL\n"
	
def searchFloors():
	if vehicleType == 0:
		print "\nYour vehicle is {}\n".format(vehicleList[vehicleType])
		for vehiclee in parkingData:
			print "Floor {} --> AVAILABLE\n\t".format(parkingData.index(vehiclee)) if vehiclee.car > 0 else "\t"
		floor = int(input("Enter the floorNum: "))
		parkVehicle(floor)
	elif vehicleType == 1:
		print "\nYour vehicle is {}\n".format(vehicleList[vehicleType])
		for vehiclee in parkingData:
			print "Floor {} --> AVAILABLE\n\t".format(parkingData.index(vehiclee)) if vehiclee.bike > 0 else "\t"
		floor = int(input("Enter the floorNum: "))
		parkVehicle(floor)
	elif vehicleType == 2:
		print "\nYour vehicle is {}\n".format(vehicleList[vehicleType])
		for vehiclee in parkingData:
			print "Floor {} --> AVAILABLE\n\t".format(parkingData.index(vehiclee)) if vehiclee.bus > 0 else "\t"
		floor = int(input("Enter the floorNum: "))
		parkVehicle(floor)
	elif vehicleType == 3:
		print "\nYour vehicle is {}\n".format(vehicleList[vehicleType])
		for vehiclee in parkingData:
			print "Floor {} --> AVAILABLE\n\t".format(parkingData.index(vehiclee)) if vehiclee.van > 0 else "\t"
		floor = int(input("Enter the floorNum: "))
		parkVehicle(floor)

def checkForAvailability():
	if vehicleType < len(vehicleList):
		searchFloors()				
	else:
		print "\nEnter Correct Vehicle Type\n"
	
def getVehicleType():
	global numb,vehicleNumber,vehicleType
	print "\n<--- VEHICLE PARKING --->"
	vehicleType = int(input("\nEnter Vehicle Type: \n\n0. Car\t1. Bike\t2. Bus\t3. Van\n\n"))
	numb = int(input("\nEnter Vehicle Number: "))
	vehicleNumber.append(numb)
	checkForAvailability()
	
def displayVehicleData():
	print "_-"*23
	print "\nFloor\tCars\tBikes\tBuses\tVans\tTotal"
	print "_-"*23
	for vehicles in parkingData:
		print "\n {}\t {}\t {}\t {}\t {}\t  {}\n".format(parkingData.index(vehicles),vehicles.car,vehicles.bike,vehicles.bus,vehicles.van,vehicles.getTotalVehicles())

def enterVehicleData():
	global parkingData,numOfFloors
	print "\n<--- ENTER VEHICLE DATA --->"
	for numOfFloors in range(3):
		print "\n    --- Floor {} ---".format(numOfFloors)
		vehicleLimit = int(input("\nEnter the number of vehicles: "))
		car,bike,bus,van = int(input("\n\tCar(s): ")),int(input("\n\tBike(s): ")),int(input("\n\tBus(es): ")),int(input("\n\tVan(s): "))
		newData = Parking(car,bike,bus,van)
		totalVehicles = newData.getTotalVehicles()
		if totalVehicles == vehicleLimit:
			parkingData.append(newData)
			print "\nDATA STORED SUCCESSFULLY"
		else:
			print "\nEnter vehicles count within {}\n".format(vehicleLimit)
			break

def getMenuOption():
	option = int(input("1. Enter Data\n2. Park my vehicle\n3. Unpark my vehicle\n4. Display Availability\n5. Exit\n\n"))
	return option

def main():
	while 1:
		print "\n<--- PARKING SYSTEM --->\n"
		option = getMenuOption()
		if option == 1:
			enterVehicleData()		
		elif option == 2:
			getVehicleType()
		elif option == 3:
			unparkVehicle()
			updateData()
		elif option == 4:
			displayVehicleData()
		elif option >= 5:
			print "BYE"
			exit()
	
if __name__ == '__main__':						
	main()