# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 17:32:31 2019

@author: Shibo
"""

path = "adult.data"
f = open(path,'r',encoding = 'utf8')
read = str(f.read())
people = read.split('\n')
age=[]
workclass=[]
fnlwgt=[]
education = []
educationnum =[]
maritalstatus =[]
occupation =[]
relationship =[]
race =[]
sex =[]
capitalgain =[]
capitalloss =[]
hoursperweek =[]
nativecountry =[]
income =[]
c=[]

import pandas as pd
#df = pd.DataFrame(columns=['','','education','education-num','fnlwgt','marital-status','occupation','relationship','race','sex','capital-gain','capital-loss','hours-per-week','native-country'])
#for d in people:
#    dataset={}
#    age.append(d.split(', ')[0])
#    workclass.append(d.split(', ')[1])
for d in people:
    num = len(d.split(', '))
    if num == 15:
        age.append(int(d.split(', ')[0]))
        workclass.append(d.split(', ')[1])
        fnlwgt.append(d.split(', ')[2])
        education.append(d.split(', ')[3])
        educationnum.append(int(d.split(', ')[4]))
        maritalstatus.append(d.split(', ')[5])
        occupation.append(d.split(', ')[6])
        relationship.append(d.split(', ')[7])
        race.append(d.split(', ')[8])
        sex.append(d.split(', ')[9])
        capitalgain.append(d.split(', ')[10])
        capitalloss.append(d.split(', ')[11])
        hoursperweek.append(int(d.split(', ')[12]))
        nativecountry.append(d.split(', ')[13])
        incomes=d.split(', ')[14]
        if incomes == '<=50K':
            income.append(0)
            c.append('green')
        else:
            income.append(1)
            c.append('red')
df = pd.DataFrame({'age':age,'workclass':workclass,'fnlwgt':fnlwgt,'education':education,'educationnum':educationnum,'maritalstatus':maritalstatus,'occupation':occupation,'relationship':relationship,'race':race,'sex':sex,'capitalgain':capitalgain,'capitalloss':capitalloss,'hoursperweek':hoursperweek,'nativecountry':nativecountry,'income':income,'c':c})

df['age'].plot(kind='kde')
#Observe the age distribution of the sample
#It can be seen from the image that the data is mainly concentrated in the age of 20 to 60 years old. In the case of older than 60 years, errors may occur due to insufficient sample size.

df[['age','income']].groupby(by='income')['age'].plot(kind='hist', stacked=True)
df[['age','income']].groupby(by='age')['income'].mean().plot(kind='line')
#Compare the proportion of higher income and lower income in different age groups.
#As can be seen from the above figure, high-income people account for the most in the 50-year-old. The proportion of high-income people from 20 to 50 years old is gradually increasing, and gradually decreasing after 50 years old.
#
df[['age','hoursperweek']].groupby(by='age')['hoursperweek'].mean().plot(kind='line')
#Analyze changes and trends in average weekly working hours as the age
#From the age of seventeen to twenty-seven, the working hours per week gradually increase. From 27 to 60 years old, working hours are about 43 hours, and working hours begain to decline after the age of 60. After the age of 70, there is a large fluctuation due to insufficient sample size.

df[['education','income']].groupby(by='education')['income'].mean().plot(kind='bar')
# Income status of people with different academic qualifications
# Obviously, the higher the education, the greater the probability of becoming a high-income group.

df[['educationnum','income']].groupby(by='educationnum')['income'].mean().plot(kind='line')
# Income status of people with different education years
# Generally speaking, the longer the education time, the higher the income.

df[['occupation','income']].groupby(by='occupation')['income'].mean().plot(kind='bar')
# Income status of people with different occupation
# Prof-specialty, Exec-managerial and Protective-serv have higher salary

df[['occupation','age']].groupby(by='occupation')['age'].mean().plot(kind='bar')
# Higher income positions do not necessarily require a higher age

df[['race','income']].groupby(by='race')['income'].mean().plot(kind='bar')
# Income status of people with different race
# White and Asian people maybe have higher salary

df[['nativecountry','income']].groupby(by='nativecountry')['income'].mean().plot(kind='barh')
# Income status of people with different nativecountries
# People from Cambodia, France, India, Iran, Japan, Taiwan and Yugoslavia have a higher probability of getting a higher salary