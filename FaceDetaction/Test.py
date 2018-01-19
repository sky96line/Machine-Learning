import os
import numpy as np
import cv2 as cv
import pickle
from sklearn.neural_network import MLPClassifier

face_detector = cv.CascadeClassifier('ObjectDetector/face.xml')

def getName(TARGET):
  f = open('Data.txt', 'r')
  names = f.read()
  names = names.split('\n')
  for chk in names[:-1]:
    if(TARGET == int(chk[0])):
      return chk[2:]
  return 'Not Found'

cap = cv.VideoCapture(0)

while True:
  ret, img = cap.read()
  img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

  face = face_detector.detectMultiScale(img,1.3,5)
  for x, y, w, h in face:
    cv.rectangle(img, (x,y), (x+w, y+h), (255,255,255), 3)
    face_img = get_face(img, x, y, w, h, 100)

  face_img = np.asarray(face_img)
  h, w = face_img.shape
  face_img = face_img.reshape(w * h)

  with open('Classifier/clf.pkl', 'rb') as f:
      clf = pickle.load(f)

  p = clf.predict([face_img])
  print p
  cv.imshow('Faces',face_img)  
  cv.waitKey(1)

# img_check = cv.imread('Faces/user-2.0.jpg', 0)

# print img_check

# img_check = np.asarray(img_check)
# h, w = img_check.shape
# img_check = img_check.reshape(w * h)

# with open('Classifier/clf.pkl', 'rb') as f:
#     clf = pickle.load(f)

# p = clf.predict([img_check])

# print p
# name = getName(p)
# print name