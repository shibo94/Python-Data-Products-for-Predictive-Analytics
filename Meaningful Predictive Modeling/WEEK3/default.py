# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 16:53:55 2020

@author: shibo
"""

import gzip
from collections import defaultdict
import string
import random

path="amazon_reviews_us_Gift_Card_v1_00.tsv"

f = open(path,'rt',encoding='utf8')

header = f.readline()
header = header.strip().split('\t')

dataset=[]
for d in f:
    fields = line.strip().split('\t')
    d['star_rating'] = int(d['star_rating'])
    d['helpful_votes'] = int(d['helpful_votes'])
    d['total_votes'] = int(d['total_votes'])
    dataset.append(d)
    
wordCount = defaultdict(int)
punctuation = set(string.punctuation)

for d in dataset:
    r =''.join([c for c in d['review_body'].lower() if not c in punctuation])
    for w in r.split():
        wordCount[w] += 1
counts = [(wordCounts[w],w) for w in wordCount]
counts.sort()
counts.reverse()

words = [x[1] for x in counts[:1000]]

wordId = dict(zip(words,range(len(words))))

def feature(datum):
    feat = [0]*len(words)
    r = ''.join([c for c in datum['review_body'].lower() if not c in punctuation])
    for w in r.split():
        if w in words:
            feat[wordId[w]] += 1
        feat.append(1)
        return feat

random.shuffle(dataset)
X = [feature(d) for d in dataset]
y = [d['star_rating'] for d in dataset]
N = len(X)
X_train = X[:N//2]
X_valid = X[N//2:3*N//4]
X_test= X[3*N//4:]
y_train = y[:N//2]
y_valid = y[N//2:3*N//4]
y_test = y[3*N//4:]
len(X),len(X_train),len(X_valid),len(X_test)

from sklearn import linear_model

def MSE(model,X,y):
    predictions = model.predict(X)
    differences=[(a-b)**2 for (a,b) in zip(predictions,y)]
    return sum(difference) / len(differences)
bestModel = None
bestMSE = None
#Keep track of which model worked the best
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