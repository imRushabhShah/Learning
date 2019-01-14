import cv2
import numpy as np

cap = cv2.VideoCapture(0)
img1 = cv2.imread('bg.jpg')



while(1):
    _, frame = cap.read()

    rows,cols,channels=frame.shape
    roi=img1[0:rows,0:cols]

    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_red = np.array([0,0,0])
    upper_red = np.array([255,100,100])
    
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(mask,mask, mask= mask)
    median = cv2.medianBlur(res,15)
    
    cv2.imshow('mask',median)

    img1_bg=cv2.bitwise_and(roi,roi,mask=cv2.bitwise_not(median))
    
    res = cv2.bitwise_and(frame,frame, mask=(median))



    cv2.imshow('mask',median)

    #kernel = np.ones((15,15),np.float32)/225
    #filter2D = cv2.filter2D(res,-1,kernel)
    #cv2.imshow('filter2D',filter2D)

    #img2_fg=cv2.bitwise_and(img2,img2,mask=(mask))

    dst=cv2.add(img1_bg,res)

    img1[0:rows,0:cols]=dst

    cv2.imshow('3',img1)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()












cv2.waitKey(0)
cv2.destroyAllWindows()
