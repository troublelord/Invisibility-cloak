
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
flag=0
bg=[]
while(1):
    
    # Take each frame
    _, frame = cap.read()
  

    #Convert BGR to RGB
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    lower_black = np.array([0,0,0])
    upper_black = np.array([35,35,35])

    # Threshold the image to get only required colors
    mask = cv2.inRange(rgb, lower_black, upper_black)
    if flag == 0:
        bg=frame #to get background
        flag=1

    
    res=np.copy(frame)
    frame[mask!=0]=bg[mask!=0]


    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',bg)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
