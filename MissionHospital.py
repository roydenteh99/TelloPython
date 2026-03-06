##-------Starting Line-------## 
from djitellopy import Tello ## This one is to get from library

##Function##

## Blow the ball with drone with straight forward movement
def step1(drone):
    drone.move_down(50)
    drone.set_speed(20)
    drone.move_forward(200) ## increase length if not far enough

def step2(drone): ## blow ball B to A 
    drone.move_forward(200)
    drone.move_right(100)
    drone.move_down(50)

def step2Alt(drone): ## blow ball A to B
    drone.move_forward(400)
    drone.move_right(100)
    drone.move_down(50)
    drone.move_back(200)



##-----Mission command------##
drone = Tello () ## this one is to instantiate the class
drone.connect() ## this one is to connect the drone 
print("Battery % :" ,drone.get_battery()) #this is one to print battery
# ##----End of drone initialisation
# ## Mission Hospital ##
drone.takeoff()
step1(drone) ## change the step accordingly (ie step1 -> step2 or  step2alt)
drone.land()





