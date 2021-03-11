import numpy as np
import cv2, os, time, math
from matplotlib import pyplot as plt

# cv2.namedWindow('test', cv2.WINDOW_NORMAL)
#cv2.imshow('test', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

d = 0
timelapse = math.trunc(time.time())
ok = False
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('out.avi', fourcc, 20.0, (640, 480))
while True:
    now = math.trunc(time.time())
    if (now % 5 != timelapse % 5):
        ok = False
        continue
    else:
        if ok == True:
            continue
        ok = True
        print(now)
    d += 1; filename = "image" + str(d).zfill(3) + ".jpg"
    # filename = "image.jpg"
    os.system("wget http://localhost:8080/?action=snapshot -O " + filename)
    img = cv2.imread(filename, 0)
    out.write(img)
    # cv2.imshow('test', img)
    # k = cv2.waitKey(1) & 0xFF
    # if k == ord('q'):
        # print(d)
        # break
    #elif k == ord('c'):
     #   d += 1
     #   cv2.imwrite('test' + str(d).zfill(2) + '.jpg', frame)
#cam.release()
cv2.destroyAllWindows()

