import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('../OpenCV/pp.jpg',1)

#gray = cv2.cvtColor(img, cv2.COLOR_BAYER_BG2GRAY)
#iarray = np.asarray(gray)

#threshold = 122

#print(iarray[0][0][0])
cv2.imshow('image',img)
