import numpy as np
import cv2 as cv
import os

img_path = 'img/'
img_name = 'NBASampleImage'
video_name = 'NBANewVideo.mp4'

frames=[x for x in os.listdir(img_path) if '.jpg' in x]
num = len(frames)

fps = 30
writer = None
show = False

try:
    for i in range(num):
        fname = img_path+img_name+str(i)+'.jpg'
        frame = cv.imread(fname)
        if show:
            cv.imshow('video', frame)
            
        if not writer:
            height, width, channels = frame.shape
            fourcc = cv.VideoWriter_fourcc('m', 'p', '4', 'v')
            writer = cv.VideoWriter(video_name, fourcc, fps, (width, height))
        
        writer.write(frame)

finally:
    writer and writer.release() 
    cv.destroyAllWindows()
    