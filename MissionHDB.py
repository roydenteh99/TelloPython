## (BTW THIS IS LINE and other lines that start with ## at the front 
## are PURELY FOR COMMENT, they do not affect the code )
##-------Starting Line-------## 
from djitellopy import Tello
import time
drone = Tello ()
drone.connect()
print("Battery % :" ,drone.get_battery())
##----End of drone initialisation

## MissionHDB##
drone.takeoff()

time.sleep(1)## make sure pause abit before taking measurementt
distanceToGround = drone.get_distance_tof() ## the variable name of distanceToGround is get be changable

##Assuming starting at the Start Box
## a loop to repeat things 4 times 
for i in range(4) :
    drone.move_forward(100)
    drone.move_right(100)
    distanceToHDB = drone.get_distance_tof()
    heightOfHDB = distanceToGround - distanceToHDB
    print(heightOfHDB)



drone.land()