import cv2
# import numpy
import matplotlib.pyplot as plt

# import matplotlib.image as mpimg
img = cv2.imread('bg.jpg',1)
# print(img)
# cv2.imshow('FRAME', img)
plt.imshow(img)
plt.show()
cv2.waitKey(1)
cv2.destroyAllWindows()
