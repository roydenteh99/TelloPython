## (BTW THIS IS LINE and other lines that start with ## at the front 
## are PURELY FOR COMMENT, they do not affect the code )

##-------Starting Line-------## 
from djitellopy import Tello ## This one is to get from library
drone = Tello () ## this one is to instantiate the class

drone.connect() ## this one is to connect the drone 
print("Battery % :" ,drone.get_battery()) #this is one to print battery
# ##----End of drone initialisation

# ## MissionPatrol##
drone.takeoff()

square = 80
##Example of the 4 direction
drone.move_right(4 * square) ## Basic Movement (Once again line after ## is for comment so dont get obessed over this)
drone.move_forward(2 * square) 
drone.move_left(2* square)
drone.move_back(1 *square)
drone.move_forward(1*square)

drone.land()