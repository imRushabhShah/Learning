import cv2
import numpy as np

cap=cv2.VideoCapture('aa_xvid.avi') #the name of cctv video for which we want to dectach any movement 
#if use web cam use 0 for primary cam 1 for secondary cam and onwards
fgbg=cv2.createBackgroundSubtractorMOG2()
while True:
    ret, frame=cap.read()
    fgmask=fgbg.apply(frame)
    cv2.imshow('original',frame)
    cv2.imshow('fg',fgmask)
    k=cv2.waitKey(30) & 0xff
    if k==27:
       break
    #ends the video only after presssing ESC
cap.release()
cv2.destroyAllWindows()
