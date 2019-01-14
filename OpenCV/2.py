import cv2
import numpy  as np

cap=cv2.VideoCapture(0)

#saving a video file
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

while True:
    ret,frame=cap.read()
    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #defining which frame to write
    out.write(frame)
    

    #output
    cv2.imshow('frame',frame)
    cv2.imshow('frame2',grey)

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        #exit on press q
        break

cap.release()
out.release()
cv2.destroyAllWindows()
