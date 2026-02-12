from djitellopy import Tello ## This one is to get from library
import time

def landAndWait(drone):
    drone.land()
    input("press enter to take off again")
    drone.takeoff()

def scanForPrime(drone):
    time.sleep(0.5) #slight pause to stabalise
    primeMissionPadNumber = [2,3,5,7]
    numberDetected = drone.get_mission_pad_id()
    print("number detected ",numberDetected)
    if numberDetected == -1 :
        print("no number detected")
        return 
    if numberDetected % 2 > 0 :
        print("Odd Number")
    else:
        print('Even number')
    if numberDetected in primeMissionPadNumber:
        print("Prime Number!!")
        landAndWait(drone)


    
drone = Tello () ## this one is to instantiate the class
drone.connect() ## this one is to connect the drone 
print("Battery % :" ,drone.get_battery())  
drone.takeoff()

drone.enable_mission_pads()

## STEP 1 ### 
drone.move_right(200)
drone.move_forward(100)
scanForPrime(drone)
## STEP 1 ###

## STEP 2 ### 
drone.move_forward(100)
drone.move_right(100)
scanForPrime(drone)
## STEP 2 ###

## STEP 3 ### 
drone.move_forward(100)
drone.move_left(100)
scanForPrime(drone)
## STEP 3 ###

## STEP 4 ### 
drone.move_forward(100)
drone.move_right(100)
scanForPrime(drone)
## STEP 4 ###

drone.land()




