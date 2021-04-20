import cv2

#cam = cv2.VideoCapture(0)
cam = cv2.VideoCapture('http://192.168.1.8:4747/video/mjpegfeed?640x480')
while True:
    check, frame = cam.read()

    cv2.imshow('video', frame)
   
    key = cv2.waitKey(1)
    if key == 27:
        break

cam.release()
cv2.destroyAllWindows()
