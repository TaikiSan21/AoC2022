# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 19:15:56 2022
puzzle 3!
"""
#%% investigating
one = 'vJrwpWtwJgWrhcsFMMfFFhFp'
one_1 = one[0:int((len(one)/2))]
one_2 = one[int((len(one)/2)):]

set(one_1).intersection(one_2)
#%% data load
f = open('data/input03.txt', 'r')
data = f.readlines()
f.close()
data = [x.replace('\n', '') for x in data]
#%% make priority dict
import string
lowers = string.ascii_lowercase
uppers = string.ascii_uppercase
alls = lowers+uppers
prior = {alls[x]: x+1 for x in range(52)}

#%% split and intersect

def split_prior(x):
    one = x[0:int(len(x)/2)]
    two = x[int(len(x)/2):]
    common = set(one).intersection(two)
    return prior[common.pop()]
#%% answe rpart one
sum([split_prior(x) for x in data])
#%% now not common between first/second half but each set of three rows

pri3 = [prior[set(data[x]).
        intersection(data[x+1]).
        intersection(data[x+2]).pop()] for x in range(0,len(data), 3)]
sum(pri3)