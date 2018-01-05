import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.metrics import classification_report
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler

digits = datasets.load_digits()

x, y = digits.data, digits.target

x_, y_ = digits.data[8], digits.target[8]

clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
                    hidden_layer_sizes=(10, 15), random_state=1)

clf.fit(x,y)

p = clf.predict([x_])
print p

print(classification_report(y_,[p]))

'''
clf.fit(x,y)

p = clf.predict([digits.data[1796]])
print(p)

plt.plot(digits.data[:1787],'g')
plt.plot(digits.data[1788:], 'b')
plt.show()
'''



'''
==================================================

import numpy as np
from sklearn.datasets import load_iris

iris = load_iris()

x = iris.data
y = iris.target

from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = .5)

from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier()

clf = clf.fit(x_train, y_train)

pred = clf.predict(x_test)


from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, pred))


from  sklearn import tree

features = [[140, 1],[130, 1],[150, 0],[170, 0]]
labels = [0, 0, 1, 1]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

print(clf.predict([[150, 0]]))
'''
