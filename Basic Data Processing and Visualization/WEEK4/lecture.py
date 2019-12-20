# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 20:35:30 2019

@author: Shibo
"""

#L1 Matrix Processing and Numpy
import numpy
import json
path = ".json"
f = open(path)
dataset = []
while len(dataset)<5000:
    dataset.append(json.loads(json.loads(f.readline())))
dataset[0]
ratings = [d['stars'] for d in dataset]
cool = [d['cool'] for d in dataset]
funny = [d['funny'] for d in dataset]
useful = [d['useful'] for d in dataset]

ratings = numpy.array(ratings)
cool = numpy.array(cool)
funny = numpy.array(funny)
useful = numpy.array(useful)
ratings

numpy.mean(ratings)
numpy.var(ratings)
numpy.stack([cool,funny,useful])
features=numpy.stack([cool,funny,useful]).T
features=numpy.matrix(features)
numpy.linalg.inv(features.T * features)
2*numpy.sin(features)+3
2*numpy.sin(features)+3 > 4
# ndarray.shape : get the shape of an array.
# reshape: change the dimensions of an array or matrix. 
# arange : create an array containing a range of numbers
# Numpy.random : generates arrays of random numbers.
# sum, min ,max, etc :reduction operations on matrices
# Eye: identity matrices. 
# trace, eig, etc: Linear algebra operations

#L2 Introduction to Data Visualization
#L3 Introduction to Matplotlib
import json
import time
path = "/review.json"
f=open(path 'r')

dataset = []
for i in range(50000):
    dataset.append(json.loads(f.readline()))
datasetWithTimeValues = []
for d in dataset:
    d['data']
    d['timeStruct'] = time.strptime(d['data'],"%Y-%m-%d")
    d['timeInt'] = time.mktime(d['timeStruct'])
    datasetWithTimeValues.append(d)

from collections import defaultdict
weekRatings = defaultdict(list)
for d in datasetWithTimeValues:
    day = d['timeStruct'].tm_wday
    weekRatings[day].append(d['stars'])
weekAverages = {}
for d in weekRatings:
    weekAverages[d]=sum(weekRatings[d]*1.0/len(weekRatings[d]))
weekAverages
x = list(weekAverages,keys())
Y=[weekAverages[x] for x in X]
import matplotlib.pylot as plt
plt.plot(X,Y)
plt.bar(X,Y)
# zoom in more to see the detail
plt.ylim(3.6, 3.8)
plt.bar(X, Y)

plt.ylim(3.6,3.8)
plt.xlabel("Weekday")
plt.ylabel("Rating")
plt.xticks([0,1,2,3,4,5,6],['S','M','T','W','T','F','S'])
plt.title("Rating as a function of weekday")
plt.bar(X,Y)

#L4 Live-coding: MatPlotLib
path = "datasets/yelp_data/review.json"
f = open(path,'r',encoding = 'utf8')
import json
import time
dataset = []
for i in range(50000):
    d = json.loads(f.readline())
    # d['data']
    d['timeStruct'] = time.strptime(d['data'],'%Y-%m-%d')
    d['timeInt'] = time.mktime(d['timeStruct'])
    dataset.append(d)
dataset[0]
from collections import defaultdict
weekRatings = defaultdict(list)
for d in dataset:
    day = d['timeStruct'].tm_wday
    weekRatings[day].append(d['stars'])
weekAverages = {}
for d in weekRatings:
    weekAverages[d] = sum(weekRatings[d])/len(weekRatings[d])
weekAverages
from matplotlib import pyplot as plt
X = list(weekAverages,keys())
X
Y= [weekAverages[x] for x in X]
plt.plot(X,Y)
plt.show() 
plt.bar(X,Y)
plt.show()
plt.ylim(3.6, 3.8)
plt,bar(X,Y)
plt.show()
plt.xlabel("Weekday")
plt.ylabel("Rating")
plt.title("Rating as a function of weekday")
plt.bar(X,Y)
plt.show()

plt.ylim(3,6, 3.8)
plt.xlabel("Weekday")
plt.ylabel("Rating")
plt.xticks([0,1,2,3,4,5,6],['S','M','T','W','T','F','S'])
plt.title("xxx")
plt.bar(X,Y)
#L5 urllib and BeautifulSoup
from urllib.request import urlopen
f = urlopen("https://www.goodreads.com/book/show/4671.The_Great_Gatsby")
html = str(f.read())
reviews = html.split('<div id="review_')[1:]
len(reviews)
review[0]

def parseReview(review):
    d={}
    d['stars'] = review.split('<span class=" staticStars notranslate" title="')[1].split['"'][0]
    d['date'] = review.split('<a class="reviewDate')[1].split('>')[1].split('<')[0]
    d['user'] = review.split('<a title="')[1].split['"'][0]
    shelves = []
    try:
        shelfBlock = review.split('<div class="uitext greyText bookshelves">')[1].split('</div>')[0]
        for s in shelfBlock.split('shelf=')[1:]:
            shelves.append(s.split('"')[0])
        d['shelves'] = shelves
    except Exception as e:
        pass
    reviewBlock = rebiew.split('<div class="reviewText stacked">')[1].split('</div')[0]
    d['reviewBlock'] = reviewBlock
    return d
reviewDict = [parseReview(r) for r in reviews]
reviewDict[0]
from bs4 import BeautifulSoup
soup = BeautifulSoup(reviewDict[0])['reviewBlock']