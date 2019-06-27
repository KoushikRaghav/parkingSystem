# PARKING SYSTEM

## Description : 

Build a real time parking system to maintain different types of vehicles, park and unpark inside the parking block.

## Goal :

1. System should be flexible to build N number of levels in order to extend their parking space.

2. Parking Head can give the vehicle count to restrict number of vehicles in that level.

3. Parking Head can restrict any type of vehicle while creating level.

     example : while creating level parking head can give 
        
      Car - 20 nos
      
      Bus - 50 nos
      
      Van - 10 nos
      
      (Here vehicle type Bike is restricted) 


## Parking Head :

1. Adds number of vehicles that are allowed to park in the parking block.

2. Provides floorwise data of vehicles.
      
       --Floor 1--
      
            Car  = 10 nos
            Bus  = 15 nos
            Van  = 2 nos
            Bike = 1 nos
      
3. Displays entire data of the parking block.

## User :

### Module #1 -->  Parking

1. Provide vehicle type.

         0 -- Car
         1 -- Bus
         2 -- Van
         3 -- Bike

2. Provide vehicle registration number.

3. Park the vehicle.

### Module #2 -->  UnParking

1. Provide vehicle registration number.

2. UnPark the vehicle.

