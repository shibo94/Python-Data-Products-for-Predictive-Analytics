# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 20:09:30 2019

@author: Shibo
"""
#L3 Regression in Python
path = '/.csv'
f = open(path,'r')
dataset = []
header = f.readline().strip().split(',')
for line in f:
    line = line.split(',')
    dataset.append(line)
N = len(dataset)
header.index('pm2.5')
header.index('TEMP')
y = [float(d[5]) for d in dataset]
dataset = [d for d in dataset if d[5] != 'NA']
y = [float(d[5]) for d in dataset]
def feature(datum):
    feat = [1, float(datum[7])]
    return feat

X = [feature(d) for d in dataset]
y[:10]
X[:10]
theta,residuals,rank,s = numpy.linalg.lstsq(X,y)
theta
[out] pm2.5 = 107.1 - 0.68*temp

def feature(datum):
    feat = [1, float(datum[7]), float(datum[8]),float(datum[10])]
    return feat
X = [feature(d) for d in dataset]
theta, residuals, rank, s = numpy.linalg.lstsq(X,y)
theta
[out] array([3.26e+03, aaa, bbb, ccc, ddd])
X=numpy.matrix(X)
y=numpy.matrix(y)
numpy.linalg.inv(X.T * X) * X.T *y.T
matrix([3.26],
        [aaa],
        [bbb],
        [ccc])
