# -*- coding: utf-8 -*-'
# L1
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

dataset = [d for d in dataset if len(d['review_body')].split()) >= 10]
    
    
#L2
    
import json
import string
path = "/home/.../review.json"
f=open(path)
d=json.loads(f.readline())
d
review = d['text']
reviewWords = review.split()
reviewWords
' '.join(reviewWords)
# String.join() is like .split() in reverse: it takes a list(here the list of words in the review), and converts them to a string, by placing the same token(gere a spacr character)in between each one

review.lower()
# conver all the characters in the string to lowercase
string.upper()
len(review) # the number of chrarcters
len(reviewWords) #words
review[:10]
-'Love the s'
reviewWords[:10]
-['Love',
 'the',
 'staff',
 'love',
 'the',
 'meat',
 ...]
reviewWords.index("pickle")
-46 # the word position
review.find("pickle")
-238 #charactersinto review that the word appears
review.count("love")
-2
review.lower().count("love")
-3

string.punctuation
[x for x in review if not x in string.punctuation]
''.join([x for x in review if not x in string.punctuation])

string.startswith()(etc.)
string.endswith()(etc.)
string.isalpha()
string.strip()
string.lstrip()
string.rstrip()

#L3 Processing Times and Dates in Python
# Time.strptime : convert a time string to a structured time object
# Time.strftime : convert a time object to a string
# Time.maketime/calendar.timegem: convert a time object to a number
# Time.gmtime: convert a number to a time object