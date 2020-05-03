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