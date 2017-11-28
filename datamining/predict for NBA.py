import pandas as pd
import numpy as np
dataset = pd.read_csv('/Users/apple/PycharmProjects/datamining/sport.csv')
#先设定infer_datetime_format为true，再进行日期转换
dataset = pd.read_csv('/Users/apple/PycharmProjects/datamining/sport.csv', infer_datetime_format=[True], parse_dates=["Date"],skiprows=0)
dataset.columns = ["Date", "Start time", "Visitor Team", "VisitorPts", "Home Team", "HomePts", "Score type", "OT?", "Notes"]
dataset["HomeWin"] = dataset["VisitorPts"] < dataset["HomePts"]
y_true = dataset["HomeWin"].values
from collections import defaultdict
won_last = defaultdict(int)
for index,row in dataset.iterrows():
    home_team = row["Home Team"]
    visitor_team = row["Visitor Team"]
    row["HomeLastWin"] = won_last[home_team]
    row["VisitorLastWin"] = won_last[visitor_team]
    dataset.ix[index] = row
    won_last[home_team] = row["HomeWin"]
    won_last[visitor_team] = not row["HomeWin"]
print(dataset)
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score
clf = DecisionTreeClassifier(random_state=14)
X_previouswins = dataset[["HomeWin"]].values
scores = cross_val_score(clf, X_previouswins, y_true, scoring = 'accuracy')
print("Accuracy: {:.1f}%".format(np.mean(scores) * 100))





