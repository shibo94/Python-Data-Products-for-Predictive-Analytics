# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

f = open("5year.arff","r")
while not "@data" in f.readline():
    pass
dataset = []
for l in f:
    if 'f' in l:
        continue
    l = l.split(',')
    values = [1] +[float(x) for x in l]
    values[-1] = values[-1] > 0
    dataset.append(values)

len(dataset)
-[3031]
sum([x[-1] for x in dataset])
-[102]
# Next let us look at some simple statistics about our data
X = [values[:-1]] for values in dataset]
y = [values[-1]] for values in dataset]
# Next we extract our features(X) and labels (y), much as we would do for a regression problem

from sklearn import linear_model
model = linear_model.LogisticRegression
model.fit(X,y)

predictions = model.predict(X)
predictions
array([False,False,False, ... ,False.False.False])

correctPredictions = predictions == y
correctPredictions
array([True, True, True, ... ,False, False, False])

sum(correctPredictions)/len(correctPredictions)

#Traing vs Testing
#We achieved fairly high accuracy using a simple classifier "off the shelf"
#But note that we're evaluting our classifier on the same data that was used to train it

sklearn.svm.SVC : support vector classifer
sklearn.tree.DesicionTreeClassifier : Decision trees
sklearn.naive_bayes: Naive Bayes
sklearn.neighbors.KNeighborsClassifier:Nearest Neighbors

#L2 Introduction to Training and Testing
f = open("5year.arff","r")
while not "@data" in f.readline():
    pass
dataset = []
for l in f:
    if 'f' in l:
        continue
    l = l.split(',')
    values = [1] +[float(x) for x in l]
    values[-1] = values[-1] > 0
    dataset.append(values)
import random
random.shuffle(dataset)
X = [values[:-1] for values in dataset]
y = [values[-1] for values in dataset]
# test set to be random samples of the data
N = len(X)
X_train = X[:N//2]
X_test = X[N//2:]
y_train = y[:N//2]
y_test = y[N//2:]

len(X), len(X_train),len(X_test)
(3031,1515,1516)

Next we train our model as before, but we use only the training data and labels

from sklearn import linear_model
model = linear_model.LogisticRefression()
model.fit(X_train, y_train)

predictionsTrain = model.predict(X_train)
predictionsTest = model.predict(X_test)

correctPredictionsTrain = PredictionsTrain == y_train
correctPredictionsTest = PredictionsTest == y_test

sum(correctPredictionsTrain) / len(correctPredictionsTrain) # Training accuracy
sum(correctPredictionsTest) / len(correctPredictionsTest)# Test  accuracy

#L3 Gradient Descent in Python
path = "datasets/PRSA_data_2010.1.1-2014.12.31.csv"
f = open(path, 'r')
dataset = []
header = f.readline().strip().split(',')
for line in f:
    line = line.split(',')
    dataset.append(line)
header.index('pm2.5')
out[5]
dataset = [d for d in dataset if d[5] != 'NA']
def feature(datum):
    feat = [1, float(datum[7])]
    return feat
