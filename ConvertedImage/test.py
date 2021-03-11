import numpy as np
import cv2
from skimage import feature, exposure
import datetime

arr = np.zeros(6561)
f = open('ans.txt', 'r')
for i in range(6561):
    arr[i] = f.readline()
f.close()
timeNow = datetime.datetime.now()
for image in range(27):
    mi = 11.0; xx = 0; yy = 0
    img = cv2.imread('test' + str(image).zfill(2) +'.jpg', 0)
    clahe = cv2.createCLAHE(clipLimit = 2.0, tileGridSize = (8, 8))
    equ = clahe.apply(img)
    for ii in range(21):
        for jj in range(7):
            frame = img[jj * 8 : jj * 8 + 88, ii * 8 : ii * 8 + 88]
            out = feature.hog(frame, visualize = False, feature_vector = True)
            compare = arr - out
            x = 0.0
            for i in compare:
                x += abs(i)
            x /= 6561.0
            if x < mi:
                mi = x; xx = ii; yy = jj
    print('min:', mi, ' at ', xx + 1, '-', yy + 1)
timeNow = datetime.datetime.now() - timeNow
print(timeNow)