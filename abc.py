import numpy as np
import cv2, os, time, math
from matplotlib import pyplot as plt

# cv2.namedWindow('test', cv2.WINDOW_NORMAL)
#cv2.imshow('test', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

d = 0
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('out.mp4', fourcc, 32.0, (640, 480))
for d in range(26):
    filename = "image" + str(d + 1).zfill(3) + ".jpg"
    img = cv2.imread(filename, 0)
    
    out.write(img)
    print(d)