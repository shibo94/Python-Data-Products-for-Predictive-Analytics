# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 10:16:59 2020

@author: shibo
"""

pred=[1, 222, 55, 77, 33, 41]
actual=[1, 21, 5, 7, 3.2, 4.2]
def MSE(pred, actual):
  n=0
  total=0
  for n in range(len(pred)):
    s=(float(pred[n])-float(actual[n]))**2
    total = total + s
  return total/(len(pred))
d=MSE(pred, actual)
print(d)