# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 17:00:27 2019

@author: Shibo
"""

import string
string_list =['hello,','world']
newwordlist = ''
for word in string_list:
    word.lower()
    newword= ''.join([x for x in word if not x in string.punctuation])
    if not newwordlist:
        newwordlist = newword
    else:
        newwordlist = newwordlist + ' ' + newword
