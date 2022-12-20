# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 10:07:15 2022

@author: taiki.sakai
"""
import numpy as np

def test_eight():   
    data = '''30373
25512
65332
33549
35390'''
    data = data.split('\n')
    data = processor_eight(data)
    count = count_vis(data)
    views = count_views(data)
    return (count, int(views.max()))

# wants list of numbers for each row
def processor_eight(x):
    # print(type(x))
    if isinstance(x, str):
        f = open(x, 'r')
        x = f.readlines()
        x = [y.replace('\n', '') for y in x]
        f.close()
    x = [list(y) for y in x]
    arr = np.array(x, dtype=int)
    return arr

def count_vis(x):
    # count outers
    shape = x.shape
    n_vis = sum(shape) * 2 - 4
    # print(n_vis)
    ix_list = []
    for i in range(1, shape[0]-1):
        row_ix = count_one(x[i, :])
        ix_list.extend([(i, y) for y in row_ix])
    # print(ix_list)   
    for j in range(1, shape[1]-1):
        col_ix = count_one(x[:, j])
        ix_list.extend([(y, j) for y in col_ix])
    # print(ix_list)
    n_vis += len(set(ix_list))
    return n_vis

def count_one(x):
    vis_ix = np.zeros(0, dtype=int)
    for i, v in enumerate(x):
        if i == 0:
            if v == 9:
                break
            continue
        if i == len(x) - 1:
            break
        if v == 9:
            vis_ix = np.append(vis_ix, i)
            break
        before = x[:i]
        if all (before < v):
            vis_ix = np.append(vis_ix, i)
    
    rev_x = np.flip(x)
    # print(rev_x)
    for i, v in enumerate(rev_x):
        if i == 0:
            if v == 9:
                break
            continue
        if i == len(x) - 1:
            break
        if v == 9:
            vis_ix = np.append(vis_ix, x.shape[0] - i - 1)
            break
        before = rev_x[:i]
        if all (before < v):
            vis_ix = np.append(vis_ix, x.shape[0] - i - 1)
            
    return np.unique(vis_ix)

def count_views(x):
    nrow, ncol = x.shape
    counts = np.zeros((nrow, ncol))
    for i in range(1,nrow-1):
        for j in range(1, ncol-1):
            this_count = 1
            left = np.flip(x[i, :j])
            this_count *= count_one_view(left, x[i,j])
            right = x[i, (j+1):]
            this_count *= count_one_view(right, x[i,j])
            up = np.flip(x[:i, j])
            this_count *= count_one_view(up, x[i,j])
            down = x[(i+1):, j]
            this_count *= count_one_view(down, x[i,j])
            counts[i,j] = this_count
    return counts

def count_one_view(x, v):
    count = 0
    for i in range(len(x)):
        count += 1
        if x[i] >= v:
            break 
    return count

def main():
    test = test_eight()
    print(test)
    data = processor_eight('../data/input08.txt')
    count = count_vis(data)
    print(count)
    views = count_views(data)
    print(views.max())
    assert test == (21, 8)
    

    
if __name__ == '__main__':
    main()