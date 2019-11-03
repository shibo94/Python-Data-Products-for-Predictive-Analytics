# -*- coding: utf-8 -*-'

import gzip
path = "/home/.../tsv.gz"
f= =gzip.open(path,'rt')

import csv
reader = csv.reader(f,delimiter = '\t')

header = next(reader)

dataset = []
for line in reader:
    d = dict(zip(header,line))
    for field in ['helpful_votes','star_rating,'total_votes']:
        d[field] = int(d[field])
    for field in ['verified_purchase','vine']:
        if d[field] == "Y":
            d[field] = True
        else:
            d[field] = False
    dataset.append(d)
    
len(dataset)

dataset[0]

dataset = [d for d in dataset if 'review_data' in d]

for d in dataset:
    d['yearInt']=int(d['review_data'][:4])
    
dataset = [d for d in dataset if d['yearInt']>2009]

dataset = [d for d in dataset if d['total_votes'] < 3 or d['helpful_votes']/d['total_votes'] >= 0.5]

from collections import defaultdict
nReviewsPerUser = defaultdict(int)
nReviewsPerUser[d['customer_id']] += 1
#fliter dataset to discard inactive users

dataset = [d for d in dataset if nReviewsPerUser[d['customer_id']]>=2]
len(dataser)
#filter to keep only users with 2 or more reviews