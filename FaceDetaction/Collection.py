import os
import cv2 as cv
import numpy as np

def get_id():
  f = open('Data.txt', 'r')
  num = f.read()
  if(num):
    num = num.split('\n')
    num = num[-2]
    z = int(num.split(',')[0]) + 1
  else:
    z=0
  f.close()
  return z

def get_face(imgs, x, y, w, h, size):
  return cv.resize(imgs[y : y+h, x : x+w],(size,size))

def write_in_file(id, name):
  f = open('Data.txt','a')
  f.write(str(i)+','+name)
  f.write('\n')
  f.close()

face_detector = cv.CascadeClassifier('ObjectDetector/face.xml')
eye_detector = cv.CascadeClassifier('ObjectDetector/eye.xml')

name = str(raw_input('Enter name : '))
cap = cv.VideoCapture('http://192.168.43.80:8080/videofeed')

i = get_id()
j = 0

while(j<100):
  ret, img = cap.read()
  img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

  face = face_detector.detectMultiScale(img,1.3,5)
  toggle = False
  for x, y, w, h in face:
    #cv.rectangle(img, (x,y), (x+w, y+h), (255,255,255), 3)
    face_img = get_face(img, x, y, w, h, 100)
    toggle = True
    cv.imwrite('Faces/user-' + str(i) + '.' + str(j) + '.jpg',face_img)
    j += 1
  if(toggle):
    cv.imshow('Faces',face_img)  
  cv.waitKey(1)

write_in_file(i,name)