import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
# img = cv.imread('ball.jpg')
# cv.imshow('n', img)

# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# ret, thresh = cv.threshold(gray,0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)

# cv.imshow('image1',thresh)

# # noise removal
# kernel = np.ones((3,3),np.uint8)
# opening = cv.morphologyEx(thresh,cv.MORPH_OPEN,kernel, iterations = 2)
# # sure background area
# sure_bg = cv.dilate(opening,kernel,iterations=3)
# # Finding sure foreground area
# dist_transform = cv.distanceTransform(opening,cv.DIST_L2,5)
# ret, sure_fg = cv.threshold(dist_transform,0.7*dist_transform.max(),255,0)
# # Finding unknown region
# sure_fg = np.uint8(sure_fg)
# unknown = cv.subtract(sure_bg,sure_fg)


# #cv.imshow('image2', unknown)


# # Marker labelling
# ret, markers = cv.connectedComponents(sure_fg)
# # Add one to all labels so that sure background is not 0, but 1
# markers = markers+1
# # Now, mark the region of unknown with zero
# markers[unknown==255] = 0

# #cv.imshow('image3',markers)

# markers = cv.watershed(img,markers)
# img[markers == -1] = [255,0,0]

# cv.imshow('niceyo',img)

# cv.waitKey(0)
# cv.destroyAllWindows()

cap = cv.VideoCapture(0)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv.imshow('frame',frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
# When everything done, release the capture

cap.release()
cv.destroyAllWindows()