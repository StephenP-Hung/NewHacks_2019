import cv2
import sys
import logging as log
import datetime as dt
from time import sleep
import email_send


class myrectangle:

    def __init__(self, x, y, width, height):
        self.x = x;
        self.y = y;
        self.height = height;
        self.width = width;

    def contains(self, x, y):
        if x >= self.x and x <= self.x+ self.width and y >= self.y and y <= self.y+ self.height:
            return True;

        else:
            return False;


cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
log.basicConfig(filename='webcam.log',level=log.INFO)

video_capture = cv2.VideoCapture(0)
anterior = 0

current_rectangles = [];
email_sent = False

while True:
    if not video_capture.isOpened():
        print('Unable to load camera.')
        sleep(5)
        pass

    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Draw a rectangle around the faces
    current_rectangles.clear();
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        current_rectangles.append(myrectangle(x,y,w,h))

    #sending email if face detected
    if len(current_rectangles) != 0 and not email_sent:
        email_send.send_email()
        email_sent = True

    if anterior != len(faces):
        anterior = len(faces)
        log.info("faces: "+str(len(faces))+" at "+str(dt.datetime.now()))


    # Display the resulting frame
    cv2.imshow('Video', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Display the resulting frame
    cv2.imshow('Video', frame)

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
