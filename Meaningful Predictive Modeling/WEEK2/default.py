# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 11:49:50 2020

@author: shibo
"""

import gzip
from collections import defaultdict
import string
import random
from nltk.stem.porter import PorterStemmer
import numpy

path = "amazon_reviews_us_Gift_Card_v1_00.tsv"

# f = gzip.open(path, 'rt', encoding="utf8")
f = open(path, 'rt', encoding="utf8")


header2 = f.readline()
header = header2.strip().split('\t')

dataset = []

for line in f:
    fields = line.strip().split('\t')
    d = dict(zip(header, fields))
    d['star_rating'] = int (d['star_rating'])
    d['helpful_votes']= int(d['helpful_votes'])
    d['total_votes'] = int(d['total_votes'])
    dataset.append(d)
    
wordCount = defaultdict(int)
punctuation = set(string.punctuation)
for d in dataset:
    r = ''.join([c for c in d['review_body'].lower() if not c in punctuation])
    for w in r.split():
        wordCount[w] += 1
print(len(wordCount))

wordCount = defaultdict(int)
punctuation = set(string.punctuation)
stemmer = PorterStemmer()
for d in dataset:
    r = ''.join([c for c in d['review_body'].lower() if not c in punctuation])
    for w in r.split():
        w = stemmer.stem(w)
        wordCount[w] += 1
print(len(wordCount))

# Excract and build features from the most common words
wordCount = defaultdict(int)
punctuation = set(string.punctuation)

for d in dataset:
    r = ''.join([c for c in d['review_body'].lower() if not c in punctuation])
    for w in r.split():
        wordCount[w] += 1

counts = [(wordCount[w],w) for w in wordCount]
counts.sort()
counts.reverse()

words = [x[1] for x in counts[:1000]]

wordID = dict(zip(words,range(len(words))))
wordSet = set(words)
#utility data is going to map each word to a unique ID. 

def feature(datum):
    feat = [0]*len(words)
    r = ''.join([c for c in datum['review_body'].lower() if not c in punctuation])
    for w in r.split():
        if w in words:
            feat[wordID[w]] += 1
    feat.append(1) #offset

random.shuffle(dataset)
X = [feature(d) for d in dataset]
y = [d['star_rating'] for d in dataset]
theta,residuals,rank,s = numpy.linalg.lstsq(X,y)
wordWeights = list(zip(theta, words + ['offset']))
wordWeights.sort()
wordWeights[:10]
wordWeights[-10:]    

