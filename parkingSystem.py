from parking import Parking
from floor import Floor
from vehicle import Vehicle

park = Parking()
vehicleList = ["Car","Bike"]

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

def getMenuOption():
	option = int(input("1. Enter Data\n2. Park my vehicle\n3. Unpark my vehicle\n4. Display Data\n5. Exit\n\n"))
	return option

def main():
	numOfFloors = 2	
	while 1:
		print "\n<--- PARKING SYSTEM --->\n"
		option = getMenuOption()
		if option == 1:
			parkingData,floorObject = park.getParkingData(vehicleList)		
		elif option == 2:
			vehicledata = getVehicleData()	
			print "\nYour vehicle is {}\n".format(vehicleList[vehicledata.getVType()])
			park.listAvailableFloors(vehicledata.getVType(),vehicledata,vehicleList) 
			floorObject.parkVehicle(parkingData,vehicledata,vehicleList)
		elif option == 3:
			floorObject.unparkVehicle(parkingData,vehicleList)
		elif option == 4:
			park.displayParkingData()
		elif option >= 5 or option == 0:
			print "BYE"
			exit()
	
if __name__ == '__main__':						
	main()