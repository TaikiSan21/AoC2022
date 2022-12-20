# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 09:28:31 2022
puzzle 12 is hard
@author: taiki.sakai
"""
import numpy as np
import string
from collections.abc import Iterable

letters = string.ascii_lowercase
height = {letters[x]: x for x in range(len(letters))}
height['S'] = 0
height['E'] = 25

def test_twelve():
    data = '''Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi'''

    data = data.split('\n')
    # data = [list(x) for x in data]
    # data = np.array(data)
    data = process_twelve(data)
    graph = Graph(data)
    graph = do_search(graph)
    
    all_a = [tuple(a) for a in np.argwhere(data == 'a')]

    all_search = [from_scratch(data, s) for s in all_a]
    print(all_search)
    print(min(all_search))
    # print(graph.nodes[(2,5)].dist)
    
    # print(node.conn)
    # print(poss_next(node, graph))
    
def from_scratch(data, start):
    graph = Graph(data)
    return do_search(graph, start)

def do_search(graph, start=None):
    if start is None:
        start = tuple(np.argwhere(graph.data == 'S')[0])
    end = tuple(np.argwhere(graph.data == 'E')[0])
    graph.nodes[start].dist = 0
    to_visit = visit_one(start, graph)
    max_visit = graph.data.shape[0] * graph.data.shape[1]
    i = 0
    while len(to_visit) > 0:
        vis_dist = {d: graph.nodes[d].dist for d in to_visit}
        dist_order = sorted(vis_dist, key=vis_dist.get)
        next_vis = visit_one(dist_order[0], graph)
        to_visit.remove(dist_order[0])
        if end in next_vis:
            break
        to_visit.extend(next_vis)
        if i > max_visit:
            break
        i += 1
    # print(graph.nodes[end].dist)
    return graph.nodes[end].dist
    # list to search next from current
    # check against visited
    # order by lowest dist
    # add to visited
    
def visit_one(current, graph):
    graph.nodes[current].visited = True
    next_nodes = poss_next(current, graph)
    next_dist = [graph.nodes[n].dist for n in next_nodes]
    curr_dist = graph.nodes[current].dist + 1
    good_nodes = [next_nodes[i] for i in range(len(next_nodes)) if
                  next_dist[i] > curr_dist]
    for n in good_nodes:
        graph.nodes[n].dist = curr_dist
    
    return good_nodes
        
        
def process_twelve(x):
    if isinstance(x, str):
        f = open(x, 'r')
        x = f.readlines()
        f.close()
    x = [y.replace('\n', '') for y in x]
    x = [list(y) for y in x]
    x = np.array(x)
    return x

def poss_next(node, graph):
    shape = graph.data.shape
    ix = graph.nodes[node].loc
    x = ix[0]
    y = ix[1]
    poss_x = [x-1, x+1]
    poss_y = [y-1, y+1]
    
    if x == shape[0]-1:
        poss_x = [x-1]
    if x == 0:
        poss_x = [x+1]
    if shape[1] == 1:
        poss_x = []
    if y == shape[1]-1:
        poss_y = [y-1]
    if y == 0:
        poss_y = [y+1]
    if shape[0] == 1:
        poss_y = []

    out = [(x, new_y) for new_y in poss_y]
    out = out + [(new_x, y) for new_x in poss_x]
    out = [x for x in out if not graph.nodes[x].visited]
    # check if we got there faster already
    # curr_count = len(path)
    # next_count = [path.count_map[o] for o in out]
    # allowed = [curr_count < c for c in next_count]
    # if any([not x for x in allowed]):
    #     print('SKIPPED!')
    # out = [out[x] for x in range(len(out)) if allowed[x]]
    # check if height diff is allowed
    curr_height = height[graph.nodes[node].value]
    next_height = [height[graph.nodes[o].value] for o in out]
    allowed = [(curr_height + 1) >= h for h in next_height]

    out = [out[x] for x in range(len(out)) if allowed[x]]
    return out
    
#%% if no paths, return cnothing. If path, direction + path for each path
# well this wasnt useful

# start path == ''
# down or right
# down has down or right
# right has up or right or down. 
     
class Node():
    def __init__(self, loc, val):
        self.loc = loc
        self.value = val
        self.conn = []
        self.dist = np.inf
        self.visited = False

class Graph():
    def __init__(self, data):
        self.data = data
        self.nodes = {}
        self.add_all()
        self.visited = []
        self.next = []
        
    def add_node(self, node):
        self.nodes[node] = Node(node, self.data[node])
    
    def add_all(self):
        shape = self.data.shape
        for i in range(shape[0]):
            for j in range(shape[1]):
                self.add_node((i, j))  
        
        # for n in self.nodes:
        #     self.nodes[n].conn = poss_next(self.nodes[n], self)
    
    def __len__(self):
        return len(self.nodes)

def main():
    data = process_twelve('../data/input12.txt')
    graph = Graph(data)
    graph = do_search(graph)
    all_a = [tuple(a) for a in np.argwhere(data == 'a')] 
    all_search = [from_scratch(data, s) for s in all_a]
    print(min(all_search))
    
if __name__ == '__main__':
    test_twelve()
    main()