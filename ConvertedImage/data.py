import cv2
from matplotlib import pyplot
from skimage import feature, exposure
import numpy as np

def analyze(picNum):
    f = open('ans.txt', 'w')
    ans = np.zeros(1215)

    for i in range(picNum):
        img = cv2.imread('head75.jpg', 0)
        clahe = cv2.createCLAHE(clipLimit = 2.0, tileGridSize = (8, 8))
        equ = clahe.apply(img)
        out = feature.hog(img, visualise = False, feature_vector = True, )
        ans = ans + out
    ans = np.true_divide(ans, picNum)
    for i in ans:
        f.write(str(i) + '\n')
    f.close()

analyze(70)

