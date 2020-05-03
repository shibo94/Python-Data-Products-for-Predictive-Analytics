# -*- coding: utf-8 -*-
"""
Created on Sat May  2 09:52:31 2020

@author: shibo
"""

import gzip
from collections import defaultdict
import random
import numpy
import scipy.optimize

path=''

f = gzip.open(path,"rt",encoding="utf8")

header = f.readline()
header = header.strip().split('\t')
dataset=[]
for line in f:
    fields = line.strip().split('\t')
    d = dict(zip(header,fields))
    d['star_rating'] = int(d['star_rating'])
    d['helpful_votes'] = int(d['helpful_votes'])
    d['total_votes'] = int(d['total_votes'])
    dataset.append(d)

usersPerItem = defaultdict(set)
itemsPerUser = defaultdict(set)
itemNames={}
for d in dataset:
    user,item = d['customer_id'],d['product_id']
    usersPerItem[item].add(user)
    itemsPerUser[user].add(item)
    itemNames[item] = d['product_title']

def Jaccard(s1,s2):
    numer = len(s1,intersection(s2))
    denom = len(s1.union(s2))
    return numer / denom

def mostSimilar(i):
    similarities=[]
    users = usersPerItem[i]
    for i2 in usersPerItem:
        if i2 == i: continue
        sim = Jaccard(users,usersPerItem[i2])
        similarities.append((sim,i2))
    similarities.sort(reverse=True)
    return similarities[:10]
dataset[2]
query = dataset[2]['product_id']
mostSimilar(query)
itemNames[query]
[itemNames[x[1]] for x in mostSimilar(query)]

def mostSimilarFast(i):
    similarities=[]
    users = usersPerItem[i]
    candidateItems = set()
    for u in users:
        candidateItems = candidateItems.union(itemsPerUser[u])
    for i2 in candidateItems:
        if i2 == i: continue
        sim = Jaccard(users,usersPerItem[i2])
        similarities.append((sim,i2))
    similarities.sort(reverse=True)
    return similarities[:10]

reviewsPerUser = defaultdict(list)
reviewsPerItem = defaultdict(list)
for d in dataset:
    user,item = d['custom_id'],d['product_id']
    reviewsPerUser[user].append(d)
    reviewsPerItem[item].append(d)
    
ratingMean = sum([d['star_rating'] for d in dataset] / len(dataset))
ratingMean

def predictRating(user,item):
    ratings=[]
    similarities = []
    for d in reviewsPerUser[user]:
        i2 = d['product_id']
        if i2 == item:continue
        rating.append(d['star_rating'])
        similarities.append(Jaccard(usersPerItem[item],usersPerItem[i2]))
    if(sum(similarities)>0):
        weightedRating = [(x*y) for x,y in zip(ratings,similarities)]
        return sum(weightedRatings) / sum(similarities)
    else:
        return ratingMean
def MSE(predictions,labels):
    differences = [(x-y)**2 for x,y in zip(predictions,labels)]
    return sum(differneces) / len(differences)

alwaysPredictMean = [ratingMean for d in dataset]
cfPredictions = [predictRating(d['customer_id'],d['product_id']) for d in dataset]
labels = [d['star_rating'] for d in dataset]
MSE(alwaysPredictMean,labels)
MSE(cfPredictions,labels)

# Implementing a Latent Factor Model
N = len(dataset)
nUsers = len(reviewsPerUser)
nItems = len(reviewsPerItem)
users = list(reviewsPerUser.keys())
items = list(reviewsPerItem.keys())

alpha = ratingMean

userBiases = defaultdict(float)
itemBiases = defaultdict(float)

#Alpha and beta(userbiases) are parameters we will fit. This code sets their initial values(alpha to the mean rating, and beta_u/beta_i to zero)
def prediction(user,item):
    return alpha+userBiases[user]+itemBiases[item]
def unpack(theta):
    global alpha
    global userBiases
    global itemBiases
    alpha = theta[0]
    userBiases = dict(zip(users,theta[1:nUsers+1]))
    itemBiases = dict(zip(items,theta[1+nUsers:]))
    
def cost(theta,labels,lamb):
    unpack(theta)
    predictions = [prediction(d['customer_id'],d['product_id']) for d in dataset]
    cost = MSE(predictions,labels)
    print('MSE = '+str(cost))
    for u in userBiases:
        cost += lamb*userBiases[u]**2
    for i in itemBiases:
        cost += lamb*itemBiases[i]**2
    return cost

def derivative(theta,labels,lamb):
    unpack(theta)
    N = len(dataset)
    dalpha = 0
    dUserBiases = defaultdict(float)
    dItemBiases = defaultdict(float)
    for d in dataset:
        u,i = d['customer_id'],d['product_id']
        pred = prediction(u,i)
        diff = pred - d['star_rating']
        dalpha += 2/N*diff
        dUserBiases[u] += 2/N*diff
        dItemBiases[i] += 2/N*diff
    for u in userBiases:
        dUserBiases[u] += 2*lamb*userBiases[u]
    for i in itemBiases:
        dItemBiases[i] += 2*lamb*itemBiases[i]
    dtheta = [dalpha] + [dUserBiases[u] for u in users] + [dItemBiases[i] for i in items]
    return numpy.array(dtheta)

scipy.optimize.fmin_l_bfgs_b