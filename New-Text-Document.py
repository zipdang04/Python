import cv2
import numpy as np
from skimage import exposure
from skimage import feature

img = cv2.imread('data13.jpg',0)
img = cv2.resize(img,None,fx=0.17,fy=0.17)
print(img.shape)
H,W = 60,55
w,h = img.shape
ahihi = img.copy()
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
for m in range(0,w-W,4):
    for n in range(0,h-H,4):
        C1 = img[m:(m+H),n:(n+W)]
#         print(C1.shape)
        M = feature.hog(C1, orientations=9, pixels_per_cell=(8, 8),cells_per_block=(2, 2), transform_sqrt=True,block_norm="L1",visualise=False)
        result = (sum((train_mean-M)**2))**0.5
        if result <= (1.1):
            cv2.rectangle(ahihi,(n,m),(n+W,m+H),255)
#         print(result)
#         cv2.rectangle(img,(n,m),(n+W,m+H),255)
#         print(H)
        cv2.imshow('image',ahihi)
        cv2.imshow('image1',C1)
        k = cv2.waitKey(1)
        if k == 27:
            break
    if k == 27:
        break
cv2.waitKey(0)
cv2.destroyAllWindows()