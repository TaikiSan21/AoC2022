# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 16:18:01 2022
puzzle 9!
@author: taiki.sakai
"""
import numpy as np

move_dict = {
    'U': [0, 1],
    'D': [0, -1],
    'R': [1, 0],
    'L': [-1, 0]
}

def test_nine():
    data = '''R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2'''
    data = data.split('\n')
    data = process_nine(data)
    H = Knot()
    T = Knot()
    locs = do_all_moves(data, H, T)
    data='''R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20'''
    data = data.split('\n')
    data = process_nine(data)
    h10 = [Knot() for i in range(10)]
    loc10 = do_all_movelist(data, h10)
    print(len(loc10))
    return len(locs)

    
def process_nine(x):
    if isinstance(x, str):
        f = open(x, 'r')
        x = f.readlines()
        f.close()
        x = [y.replace('\n', '') for y in x]
    
    x = [(y[0], int(y.split(' ')[1])) for y in x]
    return x

class Knot:
    def __init__(self):
        self.pos = np.array([0, 0])
    
    def move(self, move):
        if isinstance(move, str):
            amount = move_dict[move]
        else:
            amount = move
        self.pos = self.pos + np.array(amount)
    
    def follow(self, knot):
        diff = knot.pos - self.pos
        if is_touch(diff):
            # print('Touching!')
            return
        diff[0] = down_to_one(diff[0])
        diff[1] = down_to_one(diff[1])
        self.move(diff)
        
def parse_move(move, h, t):

    pos_list = []
    for i in range(move[1]):
        h.move(move[0])
        t.follow(h)
        pos_list.extend([(t.pos[0], t.pos[1])])
    return pos_list    

def do_all_moves(moves, h, t):
    locs = []
    for m in moves:
        locs.extend(parse_move(m, h, t))
    
    locs = set(locs)
    return locs

def parse_movelist(move, knots):
    pos_list = []
    for m in range(move[1]):
        for i, k in enumerate(knots):
            if i == 0:
                k.move(move[0])
                continue
            k.follow(knots[i-1])
        pos_list.extend([(k.pos[0], k.pos[1])])
    return pos_list

def do_all_movelist(moves, knots):
    locs = []
    for m in moves:
        locs.extend(parse_movelist(m, knots))
    
    locs = set(locs)
    return locs
    
def is_touch(x):
    abs_x = np.abs(x)
    if abs_x.sum() <= 1:
        return True
    if abs_x[0] == 1 and abs_x[1] == 1:
        return True
    return False

def down_to_one(x):
    if x > 1:
        return 1
    if x < -1:
        return -1
    return x
           
def main():
    test = test_nine()
    # print(test)
    assert test == 13
    data = process_nine('../data/input09.txt')
    H = Knot()
    T = Knot()
    locs = do_all_moves(data, H, T)
    print(len(locs))
    
    h10 = [Knot() for i in range(10)]
    loc10 = do_all_movelist(data, h10)
    print(len(loc10))
    
if __name__ == '__main__':
    main()

