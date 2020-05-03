# -*- coding: utf-8 -*-
"""
Created on Sun May  3 15:32:39 2020

@author: shibo
"""

import gzip
from collections import defaultdict
import scipy
import scipy.optimize
import numpy
import random

path='ratings.dat'
f = open(path,"rt",encoding="utf8")

dataset=[]
header = ['uid','mid','star']
for line in f:
    fields = line.strip().split('::')
    d = dict(zip(header,fields))
    d['uid'] = int(d['uid'])
    d['mid'] = int(d['mid'])
    d['star'] = int(d['star'])
    dataset.append(d)
    
usersPerMovie = defaultdict(set)
MoviesPerUser = defaultdict(set)
itemNames={}
for d in dataset:
    user,movie = d['uid'],d['mid']
    usersPerMovie[movie].add(user)
    MoviesPerUser[user].add(movie)
    #itemNames[item] = d['product_title']

def Jaccard(s1,s2):
    numer = len(s1.intersection(s2))
    denom = len(s1.union(s2))
    return numer / denom

def mostSimilar(i):
    similarities=[]
    users = usersPerMovie[i]
    for i2 in usersPerMovie:
        if i2 == i: continue
        sim = Jaccard(users,usersPerMovie[i2])
        similarities.append((sim,i2))
    similarities.sort(reverse=True)
    return similarities[:10]


reviewsPerUser = defaultdict(list)
reviewsPerMovie = defaultdict(list)

for d in dataset:
    user,movie = d['uid'], d['mid']
    reviewsPerUser[user].append(d)
    reviewsPerMovie[movie].append(d)
    
ratingMean = sum([d['star'] for d in dataset])/len(dataset)

def predictRating(user,movie):
    ratings = []
    similarities = []
    for d in reviewsPerUser[user]:
        i2 = d['mid']
        if i2 == movie: continue
        ratings.append(d['star'])
        similarities.append(Jaccard(usersPerMovie[movie],usersPerMovie[i2]))
    if (sum(similarities) > 0):
        weightedRatings = [(x*y) for x,y in zip(ratings,similarities)]
        return sum(weightedRatings) / sum(similarities)
    else:
        # User hasn't rated any similar items
        return ratingMean
    
def MSE(predictions, labels):
    differences = [(x-y)**2 for x,y in zip(predictions,labels)]
    return sum(differences) / len(differences)
cfPredictions=[]
alwaysPredictMean=[]
for d in range(100):
    alwaysPredictMean.append(ratingMean)
    user,movie = dataset[d]['uid'], dataset[d]['mid']
    cfPredictions.append(predictRating(user,movie))
labels = [d['star'] for d in dataset]
print(MSE(alwaysPredictMean, labels), MSE(cfPredictions, labels))