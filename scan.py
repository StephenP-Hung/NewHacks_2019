import numpy as np
import cv2
from matplotlib import pyplot as plt

# cap = cv.VideoCapture(0)
# while(True):
#     # Capture frame-by-frame
#     ret, frame = cap.read()
#     # Our operations on the frame come here
#     gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#     # Display the resulting frame
#     cv.imshow('frame',gray)
#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break
# # When everything done, release the capture

# cap.release()
# cv.destroyAllWindows()

def show_webcam(mirror=False):
            scale=10

            cam = cv2.VideoCapture(0)
            while True:
                ret_val, img = cam.read()
                if mirror: 
                    img = cv2.flip(img, 1)


                #get the webcam size
                height, width, channels = img.shape

                #prepare the crop
                centerX,centerY=int(height/2),int(width/2)
                radiusX,radiusY= int(scale*height/100),int(scale*width/100)

                minX,maxX=centerX-radiusX,centerX+radiusX
                minY,maxY=centerY-radiusY,centerY+radiusY

                cropped = img[minX:maxX, minY:maxY]
                resized_cropped = cv2.resize(cropped, (width, height)) 

                cv2.imshow('my webcam', resized_cropped)
                if cv2.waitKey(1) == 27: 
                    break  # esc to quit

                #add + or - 5 % to zoom

                if cv2.waitKey(1) == 0: 
                    scale += 5  # +5

                if cv2.waitKey(1) == 1: 
                    scale = 5  # +5


def main():
        show_webcam(mirror=True)

if __name__ == '__main__':
            main()