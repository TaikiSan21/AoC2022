# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 09:11:48 2022
puzzle 5!
@author: taiki.sakai
"""
#%% read data
f = open('data/input05.txt', 'r')
data = f.readlines()
f.close()
what = '''    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
'''
# what = what.split('\n')
# what[4] = '\n'
# data = what
#%% process data
import re
for i in range(len(data)):
    print(data[i])
    if data[i] == '\n':
        break

head_ix = i
head = data[0:(head_ix-1)]
head = [x.replace('\n', '') for x in head]
col = []
for i in range(0, len(head[0]), 4):
    col.append([head[x][i+1] for x in range(len(head)) if head[x][i+1] != ' '])

tail = [re.sub('\n|move |from |to ', '', x).split(' ') for x in data[(head_ix+1):]]
#%% class and methods
class Crate: 
    def __init__(self):
        self.stacks = []
    
    def add_stack(self, stack):
        self.stacks.append(stack)
    
    def move_stack(self, text):
        from_stack, to, num = int(text[1]) - 1, int(text[2]) - 1, int(text[0])
        to_move = self.stacks[from_stack][0:num]
        # print(to_move)
        to_move.reverse()
        self.stacks[to] = to_move + self.stacks[to]
        self.stacks[from_stack] = self.stacks[from_stack][num:]
        
    def move_stack2(self, text):
        from_stack, to, num = int(text[1]) - 1, int(text[2]) - 1, int(text[0])
        to_move = self.stacks[from_stack][0:num]
        # print(to_move)
        # to_move.reverse()
        self.stacks[to] = to_move + self.stacks[to]
        self.stacks[from_stack] = self.stacks[from_stack][num:]

#%% create instance
crate = Crate()
for i in range(len(col)):
    crate.add_stack(col[i])

crate.stacks
#%%
for i in range(len(tail)):
    crate.move_stack(tail[i])

tops = [x[0] for x in crate.stacks]
''.join(tops)
#%% wtf
crate.move_stack(tail[1])
crate.stacks
#%% part 2 use move_stack2 to not ereverse
crate = Crate()
for i in range(len(col)):
    crate.add_stack(col[i])

crate.stacks
for i in range(len(tail)):
    crate.move_stack2(tail[i])

tops = [x[0] for x in crate.stacks]
''.join(tops)