import cv2
import numpy as np

img = cv2.imread('pp.jpg', 1)

cv2.line(img, (0,0), (120,120), (255,255,255), 3)
cv2.circle(img, (200,200), 100, (0,255,0), 5)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()