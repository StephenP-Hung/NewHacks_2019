import numpy as np
import cv2
from matplotlib import pyplot as plt


count = 0
cv2.namedWindow('frame')



def zoom(centerX,centerY,flag):
	scale=10
	cam = cv2.VideoCapture(0)

	while True:
		ret_val, img = cam.read()
		#get the webcam size
		height, width, channels = img.shape
		#prepare the crop
		centerX,centerY=int(height/2),int(width/2)
		radiusX,radiusY= int(scale*height/100),int(scale*width/100)

		minX,maxX=centerX-radiusX,centerX+radiusX
		minY,maxY=centerY-radiusY,centerY+radiusY
		cropped = img[minX:maxX, minY:maxY]
		resized_cropped = cv2.resize(cropped, (width, height))

		cv2.imshow('frame', resized_cropped)

		if cv2.waitKey(1) == 27:
			break  # esc to quit

      

      	#add + or - 5 % to zoom

        if (flag): 
        	scale += 5  # +5

        if (not flag and scale == 15): 
            scale = 10  # normal scale

        if(not flag):
            scale = 5 # -5
            print('zoom done')


def zoom_on_press (event,x,y,flags,param):
	if event == cv2.EVENT_LBUTTONUP:
		#zoom in on
		global count
		if(count % 2 == 0):
			click_flag = True
			count += 1

		else:
			click_flag = False
			count += 1

		zoom(x,y,click_flag)
		print('zoom on press done')
	


cv2.setMouseCallback('frame', zoom_on_press)

def show_webcam():
	print('start capture')
	cap = cv2.VideoCapture(0)
	while(True):
		ret, frame = cap.read()
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		cv2.imshow('frame',gray)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break





show_webcam()



