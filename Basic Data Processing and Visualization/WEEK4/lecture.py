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