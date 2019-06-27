numb = 0
vehData = []
floorList = []
vehicleType = 0
numOfFloors = 2
parkingData = []
vehicleData = []
vehicleNumber = []
vehicleList = ["car"]

class Parking:
	def __init__(self,car,bike,bus,van):
		self.car = car
		self.bike = bike
		self.bus = bus
		self.van = van

	def getTotalVehicles(self):
		return self.car+self.bike+self.bus+self.van


def enterVehicleData():
	global parkingData,numOfFloors,vehicleList
	print "\n<--- ENTER VEHICLE DATA --->"
	# for numOfFloors in range(2):
		# print "\n    --- Floor {} ---".format(numOfFloors)
		# vehicleLimit = int(input("\nEnter the number of vehicles: "))
	for numOfFloors in range(2):
		print "\n    --- Floor {} ---".format(numOfFloors)
		vehicleLimit = int(input("\nEnter the number of vehicles: "))
		car,bike,bus,van = int(input("\n\tCar(s): ")),int(input("\n\tBike(s): ")),int(input("\n\tBus(es): ")),int(input("\n\tVan(s): "))
		parkingData.append(Parking(car,bike,bus,van))
		# import pdb; pdb.set_trace()
		#print parkingData[numOfFloors]

		totalVehicles = parkingData[numOfFloors].getTotalVehicles()
		if totalVehicles == vehicleLimit:
			print totalVehicles
			print "\nDATA STORED SUCCESSFULLY"
		else:
			print "\nEnter vehicles count within {}\n".format(vehicleLimit)
			break
	#import pdb; pdb.set_trace()

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