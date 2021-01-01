import cv2
import numpy as np
import pyautogui
cap = cv2.VideoCapture(0)#try with 1 if not working
lower_blue = np.array([100, 150, 0])
upper_blue = np.array([140, 255, 255])
prev_y=0
while(1): #video conversation for long time
    ret, frame = cap.read() #ret is a boolean variable that returns true if the frame is available
    # frame is an image array vector captured based on the default frames per second defined explicitly or implicitly
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)#Hue is the color.Saturation is the greyness,
                                                # so that a Saturation value near 0 means it is dull or grey looking.
    mask=cv2.inRange(hsv, lower_blue, upper_blue)
    contours, hierarchy= cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)#finding countours
    for c in contours:
        area=cv2.contourArea(c)
        if area>100:
            x,y,w,h=cv2.boundingRect(c)#x,y,height,width
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            if y < prev_y:
               pyautogui.press('space')
               #print("moving down")
            prev_y=y
            #print(area)
            #cv2.drawContours(frame, c, -1, (0, 255, 0), 2)  # drawing the contours
    #cv2.drawContours(frame,contours,-1,(0,255,0),2)#drawing the contours
    # gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # converting in gray(Creating a mask)
    cv2.imshow('cam', frame)
    #cv2.imshow('mask', mask)
    if cv2.waitKey(10)==ord('q'):
        break

cap.release() #do not need to continue call anymore
cv2.destroyWindow()




