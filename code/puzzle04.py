# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 19:41:35 2022
puzzle 4!
@author: tnsak
"""
#%% data
f = open('data/input04.txt', 'r')
data = f.readlines()
f.close()
data = [x.replace('\n', '') for x in data]

#%% processing

def str_to_set(x):
    splits = x.split('-')
    return set(range(int(splits[0]), int(splits[1])+1))

data_set = [(str_to_set(x.split(',')[0]),
             str_to_set(x.split(',')[1])) for x in data]
    
#%% check fully overlap

def check_full_cont(x):
    min_len = min(len(x[0]), len(x[1]))
    int_len = len(x[0].intersection(x[1]))
    
    return min_len == int_len

fulls = [check_full_cont(x) for x in data_set]
sum(fulls)

#%% check any ovrlap

def any_overlap(x):
    int_len = len(x[0].intersection(x[1]))
    
    return int_len > 0

anys = [any_overlap(x) for x in data_set]
sum(anys)