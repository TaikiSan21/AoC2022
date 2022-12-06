# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 21:54:45 2022
puzzle 6!
@author: taiki.sakai
"""
test = 'abbcde'
#%%
f = open('data/input06.txt')
data = f.readlines()
f.close()
data = data[0].replace('\n', '')
#%%
data = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
#%% 4 chars for a packet
for i in range(len(data)):
    packet = data[i:(i+4)]
    if len(set(packet)) == 4:
        break

i+4

#%% part 2

for i in range(len(data)):
    packet = data[i:(i+14)]
    if len(set(packet)) == 14:
        break

i+14
