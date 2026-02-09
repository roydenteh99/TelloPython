from djitellopy import Tello
import time
import cv2
import numpy as np

def detect_qr_code(frame):
    qcd = cv2.QRCodeDetector()
    processedFrame = frame
    retval, decoded_info, points, _ = qcd.detectAndDecodeMulti(frame)
    
    if retval :
        processedFrame = cv2.polylines(processedFrame, points.astype(int), True, (0, 255, 0), 3)
        for s, p in zip(decoded_info, points):
            processedFrame = cv2.putText(processedFrame, s, p[0].astype(int),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.imshow("QR",processedFrame)
    return retval, decoded_info

def scan(drone ,waitTimeSec = 5, scanInterval = 0.1): 
    timeTaken = 0  
    while (timeTaken < waitTimeSec) :
        detected , returnTuple = detect_qr_code(drone.get_frame_read())
        if detected :
            return int(returnTuple[0])
        else:
            timeTaken += scanInterval
            time.sleep(scanInterval)
    return 0
    


drone = Tello ()
drone.connect()

drone.stream_on()

print("Battery % :" ,drone.get_battery())
drone.takeoff()
sum = 0
drone.move_right(300)
sum += scan(drone)

for i in range(3):
    drone.move_right(100)
    drone.rotate_counter_clockwise(90)
    drone.move_right(100)
    sum+=scan()

drone.move_back(200)

if sum > 10 :
    drone.move_right(100)
drone.land()




