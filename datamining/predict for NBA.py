import pandas as pd
dataset = pd.read_csv('/Users/apple/PycharmProjects/datamining/sport.csv')
print(dataset.ix[:5])
dataset = pd.read_csv('/Users/apple/PycharmProjects/datamining/sport.csv', parse_dates=["Date"], skiprows=[0,])
dataset.columns = ["Date", "Score Type", "Visitor Team", "VisitorPts", "Home Team", "HomePts", "OT?", "Notes"]
print(dataset.ix[:5])



