from __future__ import division
import time
import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.metrics import accuracy_score
from sklearn.multiclass import OneVsRestClassifier
from sklearn.cross_validation import train_test_split
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier

def processing(data):
    ans = np.zeros(len(data[0]))
    for e in data:
        ans = np.asarray(ans) + np.array(e)
    return ans/len(data)

def fetch_teams(year=5):    # teams = fetch_teams()
    t = []
    while year <= 17:
        if year == 17:
            iter = 220
        else:
            iter = 380
        data = pd.read_csv('Data/E0 ('+str(year)+').csv')
        for i in range(iter):
            home = data.iloc[i,2].lower()
            away = data.iloc[i,3].lower()
            if home not in t:
                t.append(home)
            if away not in t:
                t.append(away)
        year += 1
    return sorted(t)

def fetch_details(year=12):
    while year <= 17:
        if year == 17:
            iter = 220
        else:
            iter = 380
        data = pd.read_csv('Data/E0 ('+str(year)+').csv')
        for i in range(iter):
            team = data.iloc[i,2].lower(), data.iloc[i,3].lower()
            HS = data.iloc[i,11]
            AS = data.iloc[i,12]
            HST = data.iloc[i,13]
            AST = data.iloc[i,14]
            HC = data.iloc[i,17]
            AC = data.iloc[i,18]
            if HS == 0 or AS == 0:
                if HS == 0:
                    details.append([HS, (AST/AS) * AST, HC, AC])
                if AS == 0:
                    details.append([(HST/HS) * HST, AS, HC, AC])
            else:
                details.append([(HST/HS) * HST, (AST/AS) * AST, HC, AC])
    
            res = data.iloc[i,9]
            if res == 'H':
                ans = 1
            elif res == 'D':
                ans = 0
            else:
                ans = -1
            result.append(ans)
        year += 1

def history(teamH, teamA, year=17):
    if year == 17:
        iter = 220
    else:
        iter = 380
    data = pd.read_csv('Data/E0 ('+str(year)+').csv')
    for i in range(iter):
        team = data.iloc[i,2].lower(), data.iloc[i,3].lower()
        if teamH == team[0] or teamA == team[1]:
            HS = data.iloc[i,11]
            AS = data.iloc[i,12]
            HST = data.iloc[i,13]
            AST = data.iloc[i,14]
            HC = data.iloc[i,17]
            AC = data.iloc[i,18]
            if HS == 0 or AS == 0:
                if HS == 0:
                    test_data.append([HS, (AST/AS) * AST, HC, AC])
                if AS == 0:
                    test_data.append([(HST/HS) * HST, AS, HC, AC])
            else:
                test_data.append([(HST/HS) * HST, (AST/AS) * AST, HC, AC])


result = []
details = []
teams = []
test_data = []

home_team = 'Swansea'.lower()
away_team = 'arsenal'.lower()

# home_team = raw_input('Enter Home : ')
# away_team = raw_input('Enter Away : ')

teams = fetch_teams()


print('Getting team history...')
fetch_details()
print('Done!... \n')

train_x, test_x, train_y, test_y = train_test_split(details, result, test_size=0.1)

# history(home_team, away_team)

# X = np.asarray(details)
# Y = np.asarray(result)

test_x = processing(test_x)
# print test_x

clf = MLPClassifier(solver='adam', alpha=1e-5, hidden_layer_sizes=(100, 150, 50, 25), random_state=1)

print('Start training...')
clf.partial_fit(train_x, train_y)
# print('Done!\n')

predictions = clf.predict([test_x])
print predictions
print clf.n_layers_