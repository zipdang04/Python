import numpy as np
import cv2, math, time
from scipy import ndimage as ndi
#from matplotlib import pyplot
from skimage import feature, exposure, filters

img = cv2.imread('idk.jpg', 0)
img = filters.sobel(img)
cv2.imshow('Test', img)
k = cv2.waitKey(0)
out= feature.hog(img, visualise = False, feature_vector = True)
for i in out:
    print(i)
cv2.imwrite('idkk.jpg', img)
cv2.destroyAllWindows() 
    
