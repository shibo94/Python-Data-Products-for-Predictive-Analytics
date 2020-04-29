# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 16:53:55 2020

@author: shibo
"""

import gzip
from collections import defaultdict
import string
import random

path=

f = gzip.open(path,'rt',encoding='utf8')

header = f.readline()
header = header.strip().split('\t')

dataset=[]
for line in f:
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
count