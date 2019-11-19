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