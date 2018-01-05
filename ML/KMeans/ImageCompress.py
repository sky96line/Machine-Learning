import cv2 as cv
from sklearn.cluster import KMeans
import numpy as np

image = cv.imread('jeni.jpg')
image = cv.resize(image,(110,110))
rows = image.shape[0]
cols = image.shape[1]

image = image.reshape(image.shape[0] * image.shape[1], 3)
kmeans = KMeans(n_clusters=128, n_init=10, max_iter=200)
kmeans.fit(image)

clusters = np.asarray(kmeans.cluster_centers_, dtype=np.uint8)
labels = np.asarray(kmeans.labels_, dtype=np.uint8)
labels = labels.reshape(rows, cols)

for i in range(len(image))
cv.imwrite('128Bit.jpg',labels)
cv.waitKey(0)

'''
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

img = cv.imread('sky.jpg',0)
print img.shape

kmeans = KMeans(2)
kmeans.fit(img)

centers = kmeans.cluster_centers_
labels = kmeans.labels_

color = ['r.','g.']
for i in range(len(img)):
  #print('Co-ordinates : ',X[i],' Labels : ',labels[i])
  plt.plot(img[i][0], img[i][1], color[labels[i]], markersize=10)

plt.scatter(centers[:, 0], centers[:,1])
plt.show()
'''
