import numpy as np
import cv2, data, math, time, os, serial
from skimage import feature, exposure

arr = np.zeros(1215)
f = open('ans.txt', 'r')
for i in range(1215):
    arr[i] = f.readline()
f.close()
f = open('log.txt', 'r')
cv2.namedWindow('Test', cv2.WINDOW_NORMAL)
d = int(f.readline()); maxCorrect = float(f.readline()); high = int(f.readline())
f = os.popen("ls /dev/ttyACM*")
usbPort = f.read(); usbPort = usbPort[0:len(usbPort) - 1]
ser = serial.Serial(usbPort, 9600)
print("connect succesfully")
while True:
    img = cv2.imread('image.jpg', 0)
    mi = 1.0; xx = 0; yy = 0
    img = cv2.flip(img, 1)
    img = cv2.resize(img, (160, 120))
    for ii in range(16):    
        for jj in range(9):
            frame = img[jj * 8 : jj * 8 + 56, ii * 8 : ii * 8 + 40]
            out= feature.hog(frame, visualise = False, feature_vector = True)
            compare = arr - out
            x = 0.0
            for i in compare:
                x += i**2
            x /= 1215.0
            x = math.sqrt(x)
            if x < mi:
                mi = x; xx = ii; yy = jj
    print('min:', mi, ' at ', xx, '-', yy)
    if mi <= maxCorrect:
        if yy > high :
            cv2.rectangle(img, (xx * 8 - 1, yy * 8 - 1), (xx * 8 + 40, yy * 8 + 56), (255, 255, 255))
        else:
            cv2.rectangle(img, (xx * 8 - 1, yy * 8 - 1), (xx * 8 + 40, yy * 8 + 56), (128, 128, 128))
    else:
        print("cant detect")
    cv2.imshow('Test', img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break
f = open('log.txt', 'w')
f.write(str(d) + '\n' + str(maxCorrect) + '\n' + str(high))
f.close()
cv2.destroyAllWindows() 
    
