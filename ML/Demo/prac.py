import matplotlib.pyplot as plt
from sklearn import svm
from sklearn import linear_model

x = [1,8,2,9,3,7.8]
y = [3,9.8,2,7,1.4,8.7]

X = zip(x,y)
Y = [0,1,0,1,0,1]

clf = svm.SVC()

clf.fit(X,Y)

p = clf.predict([(11.4,22.4)])
print(p)

fig, ax = plt.subplots()
ax.scatter(x,y)
ax.plot([x[0],y[0]],[x[5],y[5]], 'k--',4)
plt.show()
