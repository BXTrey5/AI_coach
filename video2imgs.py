import numpy as np
import cv2 as cv
import os

img_path = 'img/'

cap = cv.VideoCapture('NBAVideoSample.mp4')
   
num = 0
while cap.isOpened():
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    fout = img_path+'NBASampleImage'+str(num)+'.jpg'
    num = num+1
    print (num)
    cv.imwrite(fout,frame)
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()


