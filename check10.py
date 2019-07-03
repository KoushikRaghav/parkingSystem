from parkingClass import Parking,parkVehicle
from vehicleClass import Vehicle
from floorClass import Floor,unparkVehicle

vehicleList = ["Car","Bike"]

def searchForAvailableFloors(number,vehicleType):
	print "\nYour vehicle is {}\n".format(vehicleList[vehicleType])
	for i in range(2):
		if  parkingData.getAllData()[i].isVehicleAvailable(vehicleList[vehicleType]) == True:
			print "Floor {} --> AVAILABLE\n\t".format(i)  
		else:
			print "\t"	
	floorNum = int(input("Enter the floorNum: "))
	parkingData.getAllData()[floorNum].addVehicles(Vehicle(vehicleType,number))
	return floorNum

def displayVehicleData():
	for vehicles in range(len(parkingData.getAllData())):	
		print "\n {}\t{} ".format(vehicles,str(parkingData.getAllData()[vehicles].getFloorData()).replace("{","").replace("}", ""))

def getVehicleData():	
	print "\n<--- VEHICLE PARKING --->\n\nEnter Vehicle Type:\n"
	for vehicles in vehicleList:
		print "{}. {}".format(vehicleList.index(vehicles),vehicles)
	vehicleType = int(input("\n"))
	if vehicleType < len(vehicleList):
		number = int(input("\n\nEnter Vehicle Number: "))	
		vehicleData = Vehicle(vehicleType,number)
		return vehicleData,number,vehicleType
	else:
		print "Enter the vehicle type correctly"

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
			vehicledata,number,vehicleType = getVehicleData()	
			floorNum = searchForAvailableFloors(number,vehicleType) 
			parkVehicle(floorNum,vehicledata,vehicleType) if floorNum <= numOfFloors else "\nPARKING IS FULL IN FLOOR {}".format(floorNum)
		elif option == 3:
			unparkVehicle(vehicledata)
		elif option == 4:
			displayVehicleData()
		elif option >= 5 or option == 0:
			print "BYE"
			exit()
	
if __name__ == '__main__':						
	main()