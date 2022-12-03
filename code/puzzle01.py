# -*- coding: utf-8 -*-
"""
Aoc2022 #1!
"""
#%% read data
f = open('data/input01.txt', 'r')
data = f.readlines()
f.close()
#%% process data
import numpy as np
data = [x.replace('\n', '') for x in data]
num_list = [np.zeros(0)]
ix = 0
for i in data:
    if i == '':
        ix += 1
        num_list.extend([np.zeros(0)])
        continue
    num_list[ix] = np.append(num_list[ix], int(i))

#%% Which elf has the most calories. How many?
sum_list = [x.sum() for x in num_list]
[(i, x) for i, x in enumerate(sum_list) if x == max(sum_list)]
#%% How many are top 3 carrying
sum_list.sort(reverse=True)
sum(sum_list[0:3])  