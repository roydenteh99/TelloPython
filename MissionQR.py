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
            
    
    return decoded_info

def detection_thread(drone, test = False):
    drone.streamoff()
    time.sleep(1)
    drone.streamon()
    

    frameReader = drone.get_frame_read()

    try:
        while True :
            if test :
                cv2.imshow("test",frameReader.frame)
            else:
                detect_qr_code(frameReader.frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    finally: 
            cv2.destroyAllWindows()
            drone.streamoff()


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




