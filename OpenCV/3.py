import numpy as np
import cv2

img = cv2.imread('img.jpg',cv2.IMREAD_COLOR)

cv2.line(img,(0,0),(150,150),(255,5,20),15)

#cv2.rectangle(imgSource,(15,25 top left coordinates),(200,150 bottom right coordinates),(0,255,0  color),5 width)
cv2.rectangle(img,(15,25),(200,150),(0,255,0),5)

#cv2.circle(img,(100,63)"""center""",55"""radius""",(0,0,255),-1"""width for more than 1 or -1 t0 fill in""")
cv2.circle(img,(100,63),55,(0,0,255),-1)

pts=np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
cv2.polylines(img,[pts],True,(0,255,255),5)

font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'HEy yO mAn!',(0,130),font,1,(200,25,20),5,cv2.LINE_AA)


#show image
cv2.imshow('image',img)


cv2.waitKey(0)
cv2.destroyAllWindows()
