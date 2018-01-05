import os
import numpy as np
import cv2 as cv
from sklearn.neural_network import MLPClassifier

def get_faces(root, file_types):
  photos = []
  for cwd, folders, files in os.walk(root):
    for file in files:
      if(file.split('.')[-1] in file_types):
        photos.append(cwd + '/' + file)
  return photos


photos = get_faces('New folder', ['jpg'])

i=0
for photo in photos:
  img = cv.imread(photo, 0)
  img = cv.resize(img, (100,100))
  cv.imwrite('Faces/user-2.' + str(i) + '.jpg', img)
  i += 1

for photo in photos:
  img = cv.imread(photo, 0)
  img = cv.resize(img, (100, 100))
  cv.imwrite('Faces/user-2.' + str(i) + '.jpg', img)
  i += 1
