import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.cross_validation import train_test_split
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier

iter = 380
details = []
teams = []
pairs = []

def get_teams(f):
    for i in range(iter):
        home = f.iloc[i,2].lower()
        away = f.iloc[i,3].lower()
        if home not in teams:
            teams.append(home)
        if away not in teams:
            teams.append(away)
    return sorted(teams)

def get_details(f, home_team, away_team):
    for i in range(iter):
        home = f.iloc[i,2].lower()
        away = f.iloc[i,3].lower()
        
        if home == home_team or away == away_team:
            # HS = f.iloc[i,11]
            AS = f.iloc[i,12]
            # HST	= f.iloc[i,13]
            # AST	= f.iloc[i,14]
            # HF = f.iloc[i,15]
            # AF = f.iloc[i,16]
            # HC = f.iloc[i,17]
            # AC = f.iloc[i,18]
            # HY = f.iloc[i,19]
            # AY = f.iloc[i,20]
            # HR = f.iloc[i,21]
            # AR = f.iloc[i,22]
            # details.append([HS,AS,HST,AST,HF,AF,HC,AC,HY,AY,HR,AR])
            details.append(AS)
            pairs.append([team.index(home), team.index(away)])
    print len(pairs)

data = pd.read_csv('Data/E0 (16).csv')
team = get_teams(data)

home_team = raw_input('Enter Home : ').lower()
away_team = raw_input('Enter Away : ').lower()

get_details(data, home_team, away_team)

x = np.asarray(pairs)
y_ = np.asarray(details)
# mlb = MultiLabelBinarizer()
# y = mlb.fit_transform(y_)

train_x, test_x, train_y, test_y = train_test_split(x, y_, test_size=0.30)

clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(150, 100, 50), random_state=1)
# clf = OneVsRestClassifier(MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(100, 100), random_state=1))
clf.fit(x,y_)

# x_test = [team.index(home_team), team.index(away_team)]
predictions = clf.predict(test_x)
print predictions

my_metrics = metrics.classification_report(test_y, predictions)
print my_metrics