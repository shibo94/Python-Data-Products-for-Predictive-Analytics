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
X = [feature(d) for d in dataset]
y = [float(d[5]) for d in dataset]
X[0]
[1, -4.0]
K = len(X[0])
K
theta = [0.0]*K
theta[0] = sum(y) / len(y)
def inner(x,y):
    return sum([a*b for (a,b) in zip(x,y)])
def norm(x):
    return sum([a*a for a in x])

def derivative(X,y,theta):
    dtheta = [0.0]*len(theta)
    K = len(theta)
    N = len(X)
    MSE = 0
    for i in range(N):
        error = inner(X[i],theta)-y[i]
        for k in range(k):
            dtheta[k] += 2*X[i][k]*error/N
            MSE += error*error/N
        return dtheta, MSE
MSE： MEAN SQUARED ERROR

learningRate = 0.003
while (True):
    dtheta.MSE = derivative(X,y,theta)
    m = norm(dtheta)
    print("norm(dtheta) = " + str(m) + " MSE = " + str(MSE))
    for k in range(K):
        theta[k] -= learningRate * dtheta[k]
        if m < 0.01 : break

#L4 Gradient Descent in TensorFlow
import tensorflow as tf
path = "datasets/PRSA_data_2010.1.1-2014.12.31.csv"
f = open(path,'r')
dataset = []
header = f.readline().strip().split(',')
for line in f:
    line = line.split(',')
    dataset.append(line)

header.index('pm2.5')
dataset = [d for d in dataset if d[5] != 'NA']
def feature(datum):
    feat = [1, float(datum[7]), float(datum[8]), float(datum[10])] #Temperature, pressure, and wind speed
    return feat
X = [feature(d) for d in dataset]
y = [float(d[5]) for d in dataset]
y = tf.constant(y, shape=[len(y), 1])
K =len(X[0])

def MSE(X,y,theta):
    return tf.reduce_mean((tf.matmul(X,theta) - y) ** 2)

theta = tf.Variable(tf.constant([0,0]*K, shape=[K,1]))

Initialized to zero

optimizer = tf.train.AdamOptimizer(0.01)

Stochastic gradient descent opimizer with learning rate of 0.01

objective = MSE(X, y, theta)

train = optimizer.minimize(objective)

We want to minimize the objective

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

for iteration in range(1000):
    cvalues = sess.run([train, objective])
    print("objective = " + str(cvalues[1]))
# So, theta might have an initial value like might be a vector of zeros, but I'm also telling Tensorflow that vector is a vector of variables that I would like TensorFlow to optimize for me. So here, I'm just initializing theta to be a vector of zeros of length k, and I'm telling you that this a variable. Next is a few more boilerplate Tensorflow polarizations. I'm telling it what optimizer I'd like to use, it is what's called a Stochastic gradient descent optimizer with learning rate of 0.01 and finally, I'm telling it what is the objective I want to optimize. Okay. So I'm telling it what I would like to do is optimize the mean squared error and theta is going to be the variable that can be modified in order to minimize this. So, it's important to note that everything I've done so far is really just specifying the problem. No computation is actually performed yet.
# Start transcript at 4 minutes 0 seconds4:00
# Okay. Next is a little bit more boilerplate for initializing the optimizer. The first thing I'd do is just tell it this is an objective that should be minimized and I use this Tensorflow function to perform the initialization,
    
with sess.as_default():
    print(MSE(X, y, theta).eval())
    print(theta.eval())
    
Livecoding: Tensorflow
path = "datasets/PRSA_data_2010.1.1-2014.12.31.csv"
f = open(path, 'r')

dataset = []
header = f.readline().strip().split(',')
for line in f:
    line = line.split(',')
    dataset.append(line)

header.index('pm2.5')
dataset = [d for d in dataset if d[5] != 'NA']
def feature(datum):
    feat = [1, float(datum[7]), float(datum[8]), float(datum[10])]
    return feat

X = [feature(d) for d in dataset]
y = [float(d[5]) for d in dataset]

import tensorflow as tf
y = tf.constant(y ,shape=[len(y),1])
Second thing here is the shape operation, all that's doing is converting y to a column vector rather than a row vector.
