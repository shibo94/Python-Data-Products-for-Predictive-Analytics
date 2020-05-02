# -*- coding: utf-8 -*-
"""
Created on Sat May  2 09:52:31 2020

@author: shibo
"""

import gzip
from collections import defaultdict
import random
import numpy
import scipy.optimize

path=''

f = gzip.open(path,"rt",encoding="utf8")

header = f.readline()
header = header.strip().split('\t')
