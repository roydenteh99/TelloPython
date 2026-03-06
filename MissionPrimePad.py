from djitellopy import Tello ## This one is to get from library
import time

HEIGHT_CLEARANCE = 50

def landAndWait(drone):
    drone.land()
    numberDetected = drone.get_mission_pad_id()
    drone.go_xyz_speed_mid(0, 0, 30 ,30 ,numberDetected)
    input("press enter to take off again")
    drone.takeoff()
    drone.move_up(HEIGHT_CLEARANCE) ## NEW CODE to avoid the tall obstacle

def scanForPrime(drone):
    time.sleep(0.5) #slight pause to stabalise
    primeMissionPadNumber = [2,3,5,7]
    drone.move_down(HEIGHT_CLEARANCE) ### NEW CODE to avoid the tall obstacle
    numberDetected = drone.get_mission_pad_id()
    print("number detected ",numberDetected)
    if numberDetected == -1 :
        print("no number detected")
        ## return  ### Commented out
    if numberDetected % 2 > 0 :
        print("Odd Number")
    else:
        print('Even number')

    if numberDetected in primeMissionPadNumber:
        print("Prime Number!!")
        landAndWait(drone)
    
    else:
        drone.move_up(HEIGHT_CLEARANCE) ## NEW CODE to avoid the tall obstacle



    
drone = Tello () ## this one is to instantiate the class
drone.connect() ## this one is to connect the drone 
print("Battery % :" ,drone.get_battery())  
drone.takeoff()
drone.move_up(HEIGHT_CLEARANCE) ## NEW CODE to avoid the tall obstacle
drone.enable_mission_pads()

## Comment out the steps if you wish to skip it 
## scanForPrime only involves scanning and landing
## press enter to take off once it lands 


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




