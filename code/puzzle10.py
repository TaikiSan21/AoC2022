# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 11:14:36 2022
puzzle 10!
@author: taiki.sakai
"""
import numpy as np

def test_ten():
    data = '''addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop'''
    data = data.split('\n')
    data = process_ten(data)
    R = Register()
    # R.noop()
    # R.addx(3)
    # R.addx(-5)
    R = parse_program(R, data)
    # for i in range(20, R.cycle, 40):
    #     print(R.register[i])
    # print(R.register[20, 60, 100])
    strength = get_strength(R, 220+1)
    # print(strength)
    disp = fill_display(R)
    print(disp)
    
n_cyc = {'noop': 1,
         'addx': 2
         }

def fill_display(reg):
    disp = init_display()
    for ix, r in enumerate(reg.register):
        if ix == 0:
            continue
        dix = ((ix-1) // 40, (ix-1) % 40)
        disp[dix[0]][dix[1]] = draw_one(r, ix-1)
    disp = [''.join(x) for x in disp]
    return disp

def init_display(dim=(6,40)):
    return [['.'] * dim[1] for i in range(dim[0])]
    
def get_strength(r, max_cyc=None):
    s = 0
    if max_cyc is None:
        max_cyc = r.cycle
        
    for i in range(20, max_cyc, 40):
        s += r.register[i] * i
    return s

def parse_program(r, data):
    for d in data:
        if d[0] == 'noop':
            r.noop()
        if d[0] == 'addx':
            r.addx(d[1])
    return r

def draw_one(r, ix):
    # ix += -1
    ix = ix % 40
    if r > ix + 1:
        return '.'
    if r < ix -1:
        return '.'
    return '#'

class Register:
    def __init__(self):
        self.register = [1]
        self.current = 1
        self.cycle = 0
    
    def addx(self, value):
        self.register.extend([self.current, self.current])
        self.cycle += 2
        self.current += value
    
    def noop(self):
        self.cycle += 1
        self.register.extend([self.current])
        
def process_ten(x):
    if isinstance(x, str):
        f = open(x, 'r')
        x = f.readlines()
        f.close()
        x = [y.replace('\n', '') for y in x]
    
    x = [y.split(' ') for y in x]
    for i in x:
        if len(i) > 1:
            i[1] = int(i[1])
    return x

def main():
    data = process_ten('../data/input10.txt')
    R = Register()
    R = parse_program(R, data)
    strength = get_strength(R, 220+1)
    print(strength)
    disp = fill_display(R)
    print(disp)
    
if __name__ == '__main__':
    test = test_ten()
    main()
