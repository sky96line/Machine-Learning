from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

x = [1, 5, 1.5, 8, 1, 9]
y = [2, 8, 1.8, 8, 0.6, 11]

X = zip(x,y)

kmeans = KMeans(4)
kmeans.fit(X)

centers = kmeans.cluster_centers_
labels = kmeans.labels_

color = ['r.','g.','b.','c.']
for i in range(len(X)):
  #print('Co-ordinates : ',X[i],' Labels : ',labels[i])
  plt.plot(X[i][0], X[i][1], color[labels[i]], markersize=10)

plt.scatter(centers[:, 0], centers[:,1])
plt.show()
