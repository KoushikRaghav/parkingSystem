vehicleData = []
floorData = []
numb = 0
vehData = []
vehicleType = 0
numOfFloors = 3
parkingData = []
numbcar = 0
vehicleNumber = []
vehicleList = ["Car","Bike","Bus","Van"]

class Parking:
	def __init__(self,car,bike,bus,van):
		self.car = car
		self.bike = bike
		self.bus = bus
		self.van = van

	def getTotalVehicles(self):
		return self.car+self.bike+self.bus+self.van

class Car:
	def __init__(self,car,carNum,carFloor):
		self.car = car
		self.carNumber = carNum
		self.CFloor = carFloor	

	def getFloor(self):
		return self.CFloor

	def getNumber(self):
		return self.carNumber

def parkVehicle(floor):
	global floorData,vehicleData,vehData
	floorData = parkingData[floor]
	if vehicleType == 0:
		vehicleData = Car(numbcar,numb,floor)
		vehData.append(vehicleData)
		print "\n  !! Your {} is parked !!".format(vehicleList[vehicleType])
		print "\n\t{} Number: {}".format(vehicleList[vehicleType],vehicleData.getNumber())
		print "\n\tFloor: {}".format(vehicleData.getFloor())
		if floorData.car != 0:
			floorData.car -= 1
			print "\n\t!!! PARKED !!!"
			print "{}".format(floorData.car)
		else:
			print "\nPARKING FULL\n"

def searchFloors():
	if vehicleType == 0:
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
	print "\nFloor\tCars\tTotal"
	print "_-"*23
	for vehicles in parkingData:
		print "\n {}\t {}\n".format(parkingData.index(vehicles),vehicles.car)

def enterVehicleData():
	global parkingData,numOfFloors,numbcar
	print "\n<--- ENTER VEHICLE DATA --->"
	for numOfFloors in range(3):
		print "\n    --- Floor {} ---".format(numOfFloors)
		vehicleLimit = int(input("\nEnter the number of vehicles: "))
		numbcar = int(input("\n\tCar(s): "))
		newData = Car(numbcar,0,0)
		totalVehicles = numbcar
		#totalVehicles = newData.getTotalVehicles()
		if totalVehicles == vehicleLimit:
			parkingData.append(newData)
			print "\nDATA STORED SUCCESSFULLY"
		else:
			priSnt "\nEnter vehicles count within {}\n".format(vehicleLimit)
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