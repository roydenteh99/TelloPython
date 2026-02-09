import cv2
import numpy as np
import time
from djitellopy import Tello

# Define color dictionary: {Name: (Lower, Upper)}
# Note: Red is handled by combining two masks

def detect_shape(mask, display_frame, colorName = "Input Color" ,colorRGB = (0,0,0)):
    # Use the mask directly. No need for cv2.threshold(img, 127...)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        # Ignore tiny specks of noise
        if cv2.contourArea(cnt) < 1000: 
            continue
            
        perimeter = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.04 * perimeter, True)
        
        num_corners = len(approx)
        
        if num_corners == 3:
            label = colorName + "Triangle"
            color = colorRGB 
        elif num_corners == 4:
            label = colorName + "Square"
            color = colorRGB 
        else:
            continue

        # Draw on the COLOR frame, not the mask
        cv2.drawContours(display_frame, [approx], 0, color, 5)
        
        # Put text label above the shape
        x, y, w, h = cv2.boundingRect(approx)
        cv2.putText(display_frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    return display_frame


def get_red_mask(hsv_img):
    mask1 = cv2.inRange(hsv_img, (0, 200, 100), (10, 255, 255))
    mask2 = cv2.inRange(hsv_img, (160, 200, 100), (180, 255, 255))
    return cv2.bitwise_or(mask1, mask2)

def arrayOfColorAndMask(img) :
    return_array = []
    colors = {
    "Yellow": ((20, 100, 100), (35, 255, 255)),
    "Green":  ((35, 40, 40), (85, 255, 255)),
    "Blue":   ((100, 150, 0), (140, 255, 255))
    }

    colorRGB = {
    "Yellow": (0,255,255),
    "Green":  (0,255,0),
    "Blue":   (255,0,0),
    "Red" : (0,0,255)
    }

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    for color_name, (lower, upper) in colors.items():
        mask = cv2.inRange(hsv, lower, upper)
        # CLEAN UP: Remove small dots (noise) from the mask
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)
        return_array.append([color_name, mask ,colorRGB[color_name]])
    
    return_array.append(["Red", get_red_mask(hsv) , colorRGB["Red"]])
    return return_array
    

def detect_simple_col_shapes(frame):
    processed_frame = frame
    for colorAndMask in arrayOfColorAndMask(processed_frame) :
        processed_frame = detect_shape(colorAndMask[1], processed_frame ,colorAndMask[0], colorAndMask[2])
    cv2.imshow("ColorShapeDetection",processed_frame)

def scan(drone,waitTimeSec = 5, scanInterval = 0.1): 
    timeTaken = 0  
    while (timeTaken < waitTimeSec) :
        detect_simple_col_shapes(drone.get_frame_read())
        timeTaken += scanInterval
        time.sleep(scanInterval)
    return 0