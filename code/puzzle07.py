# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 08:41:21 2022
puzzle 7!
@author: taiki.sakai
"""

f = open('data/input07.txt', 'r')
data = f.readlines()
f.close()
data = [x.replace('\n', '') for x in data]
#%% dir class

class Directory:
    
    def __init__(self, cwd, parent=None):
        self.parent = parent
        self.cwd = cwd
        self.dirs = {}
        self.files = {}
        self.size = 0
    
    def add_files(self, split):
        if split[0] == 'dir':
            self.dirs[split[1]] = Directory(cwd=split[1], parent=self)
        else:
            self.files[split[1]] = int(split[0])
            self.size += int(split[0])
    
# class DirNode:
    
#     def __init__(self, name):
#         self.name = name
#         self.files = {}
#         self.dirs = []
#         self.size = 0
    
#     def add_file(self, file):
#         split = file.split(' ')
#         if split[0] == 'dir':
#             self.dirs.append(DirNode(name=split[1]))
#         else:
#             self.files[split[1]] = int(split[0])
#             self.size += int(split[])
#%% test dir class

d1 = Directory(cwd='/')
d1.add_files(data[2])
d1.files
d1.add_files(data[4])
d1.dirs
#%% parse text
directory = None
for i, v in enumerate(data):
# for i, v in enumerate(data[0:10]):
    if directory is None:
        split = v.split(' ')
        directory = Directory(cwd=split[2])
        cur_dir = directory
        continue
    split = v.split(' ')
    if split[0] == '$':
        if split[1] == 'cd':
            if split[2] == '..':
                cur_dir = cur_dir.parent
            else:
                cur_dir = cur_dir.dirs[split[2]]
            continue
        if split[1] == 'ls':
            continue
    cur_dir.add_files(split)

#%% parse sizes. FACK i need TOTAL for each dir. Not just size of each dir

def calc_dir_size(directory):
    size = [directory.size]
    if len(directory.dirs) == 0:
        return size
    sub_size = [calc_dir_size(directory.dirs[x]) for x in directory.dirs]
    # size[0] = size[0] + np.array(sub_size).sum()
    for d in sub_size:
        # print(d)
        size[0] = size[0] + d[0]
        size.extend(d)
    
    # sub_size = [calc_dir_size(directory.dirs[x]) for x in directory.dirs]
    # sub_size.append(size)
    
    return size
#%%
import numpy as np
sizes = np.array(calc_dir_size(directory))
sizes
sizes[sizes < 100000].sum()
#%% part 2 need 30000000 free
current_free = 70000000 - sizes[0]
needed = 30000000 - current_free
sizes[sizes > needed].min()
        