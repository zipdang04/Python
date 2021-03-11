import numpy
import cv2

cv2.namedWindow('Test', cv2.WINDOW_NORMAL)
cam = cv2.VideoCapture(0)
haar = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
# haar = cv2.CascadeClassifier('HS.xml')
t = 0; dem = 0
print(haar.empty())
while True:
    ret, frame = cam.read()
    frame = cv2.flip(frame, 1)
    # frame = cv2.resize(frame, (160,120))
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = haar.detectMultiScale(img, scaleFactor = 1.2, minNeighbors = 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0))
        t += 1; dem += faces.size()
    cv2.imshow('Test', frame)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()