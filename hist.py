import cv2
import numpy
from matplotlib import pyplot as plt

for i in range(20):
    img = cv2.imread('test'+ str(i + 1).zfill(2) +'.jpg', 0)
    # equ = cv2.equalizeHist(img)
    clahe = cv2.createCLAHE(clipLimit = 2.0, tileGridSize = (8, 8))
    equ = clahe.apply(img)
    cv2.imwrite('conv' + str(i + 1).zfill(2) + '.jpg', equ)
    # hist = cv2.calcHist([equ], [0], None, [256], [0, 256])
    # plt.imshow(img, cmap = 'gray'); plt.show()
    # plt.plot(hist); plt.show()

    # color = ('b', 'g', 'r')
    # for i, col in enumerate(color):
    #     hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    #     plt.plot(hist, color = col)
    #     plt.xlim([0, 256])
    # plt.show()

    # cdf = hist.cumsum()
    # cdf_normalized = cdf * hist.max() / cdf.max()
    # plt.imshow(equ, cmap = 'gray')
    # plt.show()
    # plt.plot(cdf_normalized, color = 'b')
    # plt.hist(equ.flatten(), 256, [0, 256], color = 'r')
    # plt.xlim([0, 256])
    # plt.show()