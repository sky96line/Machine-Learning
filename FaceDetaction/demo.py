import os
import cv2 as cv
import numpy as np

face_detector = cv.CascadeClassifier('ObjectDetector/face.xml')
eye_detector = cv.CascadeClassifier('ObjectDetector/eye.xml')

cap = cv.VideoCapture('http://192.168.43.80:8080/videofeed')

j=0
while(j<100):
  ret, img_o = cap.read()
  img = cv.cvtColor(img_o, cv.COLOR_BGR2GRAY)

  face = face_detector.detectMultiScale(img,1.3,3)
  for x, y, w, h in face:
    cv.rectangle(img_o, (x,y), (x+w, y+h), (255,255,255), 3)
  cv.imshow('Look',img_o)
  j+=1
  if cv.waitKey(1) & 0xFF == ord('q'):
        break
