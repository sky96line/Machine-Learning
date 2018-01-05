import cv2
import numpy as np
import time
face_case = cv2.CascadeClassifier('face.xml')

eye_case = cv2.CascadeClassifier('eye.xml')

car_case = cv2.CascadeClassifier('cars.xml')

plat_case = cv2.CascadeClassifier('licence_plate.xml')

cap = cv2.VideoCapture('../m.mp4')

rate = 0
t = time.time()
while True:
  if(time.time()-t > 1):
    t = time.time()
    print(rate)
    rate = 0

  rate += 1
  _, img = cap.read()

  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

  faces = face_case.detectMultiScale(gray, 1.2, 3)
  for x, y, w, h in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)

  cv2.imshow('Image', img)

  if(cv2.waitKey(30) >= 0):
    break

cap.release()
cv2.destroyAllWindows()
'''
eyes = eye_case.detectMultiScale(gray, 1.3, 5)
  for x, y, w, h in eyes:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
'''
