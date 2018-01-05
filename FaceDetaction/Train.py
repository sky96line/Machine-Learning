import os
import numpy as np
import cv2 as cv
from sklearn.neural_network import MLPClassifier

clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
                    hidden_layer_sizes=(150, 100, 50, 25), random_state=1)


def get_faces(root, file_types):
  photos = []
  for cwd, folders, files in os.walk(root):
    for file in files:
      if(file.split('.')[-1] in file_types):
        photos.append(cwd + '/' + file)
  return photos


photos = get_faces('Faces', ['jpg'])

FaceList = []
IDs = []
for photo in photos:
  img = cv.imread(photo, 0)
  img = cv.adaptiveThreshold(
      img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 115, 1)
  img = np.asarray(img)
  FaceList.append(img)
  ID = int(photo.split('.')[1])
  IDs.append(ID)

IDs = np.asarray(IDs)
FaceList = np.asarray(FaceList)

n, w, h = FaceList.shape
FaceList = FaceList.reshape(n, (w * h))

print('Training Start...!')
clf.fit(FaceList, IDs)
print('Done...!')

import pickle
with open('Classifier/clf.pkl', 'wb') as f:
  pickle.dump(clf, f)
