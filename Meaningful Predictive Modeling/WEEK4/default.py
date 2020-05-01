# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 20:30:31 2020

@author: shibo
"""

import csv 
import numpy as np 
from sklearn import linear_model
import random

path = "Admission_Predict.csv" 
csv_file = open(path, mode='r') 
reader = csv.reader(csv_file,delimiter=",")
headers = next(reader)

X = [] 
Y = []
data = []
for row in reader: 
    x_values = row[1:] 
    values = [float(value) for value in x_values] 
    if values[6] == float(1): 
        values[6] = True 
    else: values[6] = False 
    data.append(values)

random.shuffle(data)
N = len(data)
X = [x[:7] for x in data] 
Y = [x[7] for x in data]

X_train = X[:3*N//5]
X_valid = X[3*N//5:4*N//5]
X_test= X[4*N//5:]
y_train = Y[:3*N//5]
y_valid = Y[3*N//5:4*N//5]
y_test = Y[4*N//5:]

def MSE(model,X,y):
    predictions = model.predict(X)
    differences=[(a-b)**2 for (a,b) in zip(predictions,y)]
    return sum(differences) / len(differences)
bestModel = None
bestMSE = None

for lamb in [0.01,0.1,1,10,100]:
    model = linear_model.Ridge(lamb,fit_intercept=False) #Fit a model for each lambda value
    model.fit(X_train,y_train)
    
    mseTrain = MSE(model,X_train,y_train)
    mseValid = MSE(model,X_valid,y_valid)
    
    print("lambda = "+str(lamb) + ', training/validation error ='   + str(mseTrain) + '/' +str(mseValid))
    if not bestModel or mseValid < bestMSE:
        bestModel = model
        bestMSE = mseValid
mseTest = MSE(bestModel,X_test,y_test)
print("test error = " + str(mseTest))