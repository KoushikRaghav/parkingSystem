from parking import Parking
from vehicle import Vehicle

vehicleData = []
floorData = []
numb = 0
vehData = []
vehicleType = 0
numOfFloors = 3
parkingData = []
vehicleNumber = []
vehicleList = ["car","bike","bus","van"]

def updateData():
	for unPark in vehData:
		if unPark.getVTtype() == 0:
			floorData.car += 1
	elif unPark.getVTtype() == 1:
		floorData.bike += 1
	elif unPark.getVTtype() == 2:
		floorData.bus += 1
	elif unPark.getVTtype() == 3:
		floorData.van += 1

def unparkVehicle():
	print "\n<--- VEHICLE UNPARKING --->"
	getVehNum = int(input("\nEnter your vehicle number: "))
	if getVehNum in vehicleNumber:
		print "\nYour vehicle is found"
		for unPark in vehData:
			print "\n\tFloor: {}".format(unPark.getFloor())
			print "\n\tVehicle Type: {}".format(vehicleList[unPark.getVTtype()])
			print "\n\tVehicle Number: {}".format(unPark.getNumber())
			print "\n\t!!! UNPARKED !!!"		
	else:
	 	print "\nYour vehicle is not found"
	
def parkVehicle(floor):
	global floorData,vehicleData,vehData
	floorData = parkingData[floor]
	vehicleData = Vehicle(vehicleType,numb,floor)
	vehData.append(vehicleData)
	if vehicleType == 0:
		print "\n  !! Your {} is parked !!".format(vehicleList[vehicleType])
		print "\n\t{} Number: {}".format(vehicleList[vehicleType],vehicleData.getNumber())
		print "\n\tFloor: {}".format(vehicleData.getFloor())
		if floorData.car != 0:
			floorData.car -= 1
			print "\n\t!!! PARKED !!!"
			print "{}".format(floorData.car)
			print "{}".format(floorData.getTotalVehicles())
		else:
			print "\nPARKING FULL\n"
	elif vehicleType == 1:
		print "\n  !! Your {} is parked !!".format(vehicleList[vehicleType])
		print "\n\t{} Number: {}".format(vehicleList[vehicleType],vehicleData.getNumber())
		print "\n\tFloor: {}".format(vehicleData.getFloor())
		if floorData.bike != 0:
			floorData.bike -= 1
			print "\n\t!!! PARKED !!!"
			print "{}".format(floorData.bike)
			print "{}".format(floorData.getTotalVehicles())
		else:
			print "\nPARKING FULL\n"
	elif vehicleType == 2:
		print "\n  !! Your {} is parked !!".format(vehicleList[vehicleType])
		print "\n\t{} Number: {}".format(vehicleList[vehicleType],vehicleData.getNumber())
		print "\n\tFloor: {}".format(vehicleData.getFloor())
		if floorData.bus != 0:
			floorData.bus -= 1
			print "\n\t!!! PARKED !!!"
			print "{}".format(floorData.bus)
			print "{}".format(floorData.getTotalVehicles())
		else:
			print "\nPARKING FULL\n"
	elif vehicleType == 3:
		print "\n  !! Your {} is parked !!".format(vehicleList[vehicleType])
		print "\n\t{} Number: {}".format(vehicleList[vehicleType],vehicleData.getNumber())
		print "\n\tFloor: {}".format(vehicleData.getFloor())	
		if floorData.van != 0:
			floorData.van -= 1
			print "\n\t!!! PARKED !!!"
			print "{}".format(floorData.van)
			print "{}".format(floorData.getTotalVehicles())
		else:
			print "\nPARKING FULL\n"
	
def searchFloors():
	if vehicleType == 0 or vehicleType == 1 or vehicleType == 2 or vehicleType == 3:
		print "\nYour vehicle is {}\n".format(vehicleList[vehicleType])
		for vehiclee in parkingData:
			print "Floor {} --> AVAILABLE\n\t".format(parkingData.index(vehiclee)) if vehiclee.car > 0 else "\t"
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