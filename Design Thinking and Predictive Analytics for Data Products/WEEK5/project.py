# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 18:15:11 2020

@author: shibo
"""

f = open("processed.cleveland.data","r")
dataset = []
for line in f:
    line = f.readline()
    line = line.strip('\n').split(',')
    dataset.append(line)
dataset = dataset[0:-1]

def feature(datum):
    #feat = [1, float(datum[0]), float(datum[1]), float(datum[11]), float(datum[12])]
    feat = [1, float(datum[0]), float(datum[1]), float(datum[2]), float(datum[3]), float(datum[4]), float(datum[5]), float(datum[6]), float(datum[7]), float(datum[8]), float(datum[9]), float(datum[10]), float(datum[11]), float(datum[12])]
    return feat    

import random
dataset_train = random.shuffle(dataset)
X = [feature(d) for d in dataset if d[11] != '?' and  d[12] != '?']
y = [float(d[13]) for d in dataset if d[11] != '?' and  d[12] != '?']

N = len(X)
X_train = X[:N//2]
X_test = X[N//2:]
y_train = y[:N//2]
y_test = y[N//2:]

import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
y_train = tf.constant(y_train ,shape=[len(y_train),1])
K = len(X[0])
def MSE(X, y,theta):
    return tf.reduce_mean((tf.matmul(X_train,theta) - y_train)**2)
theta = tf.Variable(tf.constant([0.0]*K,shape=[K,1]))
optimizer = tf.train.AdamOptimizer(0.01)
objective = MSE(X_train,y_train,theta)
train = optimizer.minimize(objective)
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

for iteration in range(10000):
    cvalues = sess.run([train,objective])
    print("objective = =" + str(cvalues[1]))
    
with sess.as_default():
    print(MSE(X,y,theta).eval())
    print(theta.eval())