import numpy as np
import cv2
from matplotlib import pyplot
from skimage import feature, exposure
import data
import math

arr = np.zeros(1215)
f = open('ans.txt', 'r')
for i in range(1215):
    arr[i] = f.readline()
f.close()
f = open('log.txt', 'r')
cv2.namedWindow('Test', cv2.WINDOW_NORMAL)
# cam = cv2.VideoCapture(1)
cam = cv2.VideoCapture(1)
dung = 0; sai = 0; d = int(f.readline()); maxCorrect = float(f.readline())
while True:
    f = open('ans.txt', 'r')
    for i in range(1215):
        arr[i] = f.readline()
    f.close()
    mi = 1.0; xx = 0; yy = 0
    ret, img = cam.read()
    img = cv2.flip(img, 1)
    img = cv2.resize(img, (160, 120))
    for ii in range(16):    
        for jj in range(9):
            frame = img[jj * 8 : jj * 8 + 56, ii * 8 : ii * 8 + 40]
            out= feature.hog(frame, visualize = False, feature_vector = True, multichannel = True)
            compare = arr - out
            x = 0.0
            for i in compare:
                x += i**2
            x /= 1215.0
            x = math.sqrt(x)
            if x < mi:
                mi = x; xx = ii; yy = jj
    print('min:', mi, ' at ', xx, '-', yy)
    show = mi <= maxCorrect
    if show:
        if yy > 2:
            cv2.rectangle(img, (xx * 8 - 1, yy * 8 - 1), (xx * 8 + 40, yy * 8 + 56), (0, 0, 255))
        else:
            cv2.rectangle(img, (xx * 8 - 1, yy * 8 - 1), (xx * 8 + 40, yy * 8 + 56), (0, 255, 0))
    cv2.imshow('Test', img)
    k = cv2.waitKey(0) & 0xFF

    if k == ord('q'):
        break
    elif k == ord('c'):
        dung += 1
        if show:
            d += 1
            frame = img[yy * 8 : yy * 8 + 56, xx * 8 : xx * 8 + 40]
            cv2.imwrite('head' + str(d).zfill(2) +'.jpg', frame)
            maxCorrect = max(maxCorrect, mi)
            data.analyze(d)
    elif k == ord('n'):
        dung += 1
        maxCorrect = max(maxCorrect, mi)
    elif k == ord('w'):
        if show:
            sai += 1
        else:
            if yy > 2:
                cv2.rectangle(img, (xx * 8 - 1, yy * 8 - 1), (xx * 8 + 40, yy * 8 + 56), (0, 0, 255))
            else:
                cv2.rectangle(img, (xx * 8 - 1, yy * 8 - 1), (xx * 8 + 40, yy * 8 + 56), (0, 255, 0))
            k = cv2.waitKey(0) & 0xFF
            if k == ord('c'):
                dung += 1; d += 1
                frame = img[yy * 8 : yy * 8 + 56, xx * 8 : xx * 8 + 40]
                cv2.imwrite('head' + str(d).zfill(2) +'.jpg', frame)
                maxCorrect = max(maxCorrect, mi)
                data.analyze(d)
            else:
                sai += 1

print('Correct: ', dung, '; Wrong: ', sai)
print('Percentage of correct answer:', float(dung * 100) / float(dung + sai))
f.close()
f = open('log.txt', 'w')
f.write(str(d) + '\n' + str(maxCorrect))
cam.release()
cv2.destroyAllWindows()     