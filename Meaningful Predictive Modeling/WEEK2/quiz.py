# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 18:16:32 2020

@author: shibo
"""

from collections import defaultdict
import string

words="A man, a plan, a canal: Panama"
wordslist=list(words.lower())
wordslist.sort(reverse=True)
wordsrev=''.join(wordslist)
wordCount = defaultdict(int)
punctuation = set(string.punctuation)
for d in wordsrev:
    if not d in punctuation:
        wordCount[d] += 1
answer=[]
for k, v in sorted(wordCount.items(), key=lambda item: item[1],reverse=True):
    answer.append((v,k))