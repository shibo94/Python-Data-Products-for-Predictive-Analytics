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