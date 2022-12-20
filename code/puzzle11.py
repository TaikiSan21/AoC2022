# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 21:21:05 2022
puzzle 11!
@author: taiki.sakai
"""
import numpy as np

def test_eleven():
    all_tests = [23, 19, 13, 17]
    M = [Monkey([79, 98], op=lambda x: mod_mult(x, 19), test=[23, 2, 3], all_tests=all_tests),
         Monkey([54, 65, 75, 74], op=lambda x: mod_add(x, 6), test=[19, 2, 0], all_tests=all_tests),
         Monkey([79, 60, 97], op=lambda x: mod_mult(x, x), test=[13, 1, 3], all_tests=all_tests),
         Monkey([74], op=lambda x: mod_add(x, 3), test=[17, 0, 1], all_tests=all_tests)]
    # print(M[0].items)
    M, c = inspect_full(M, 1000)
    print(c)
    c = np.sort(c)
    print(c[-1] * c[-2])
    it_list = [x.items for x in M]
    
    # M = [Monkey([79, 98], op=lambda x: x * 19, test=[23, 2, 3]),
    #      Monkey([54, 65, 75, 74], op=lambda x: x + 6, test=[19, 2, 0]),
    #      Monkey([79, 60, 97], op=lambda x: x * x, test=[13, 1, 3]),
    #      Monkey([74], op=lambda x: x + 3, test=[17, 0, 1])]
    # M, c = inspect_full2(M, rounds=20)
    ### TODO: all operators implemented modulo test conds
    # is broken? values do not match
    # dict it up for the modulos
    it_list = [x.items for x in M]
    print(it_list)
    
def monkey_tester(cond, t, f):
    return lambda x: t if x[cond] == 0 else f

def inspect_full(monk_list, rounds=20):
    counts = np.zeros(len(monk_list))
    for i in range(rounds):
        monk_list, c = inspect_round(monk_list)
        counts = counts + c
    
    return monk_list, counts


def inspect_round(monk_list):
    counts = np.zeros(len(monk_list))
    for i, m in enumerate(monk_list):
        for j in range(len(m.items)):
            to_m, it = m.inspect()
            monk_list[to_m].add_item(it)
            counts[i] += 1
    return monk_list, counts

def mod_dict(val, tests):
    return {t: val % t for t in tests}

def mod_mult(x, y):
    if isinstance(y, int):
        return {d: (x[d] * y) % d for d in x}
    return {d: (x[d] * y[d]) % d for d in x}

def mod_add(x, y):
    if isinstance(y, int):
        return {d: (x[d] + y) % d for d in x}
    return {d: (x[d] + y[d]) % d for d in x}
    
def mod_div(x, y):
    if isinstance(y, int):
        return {d: (x[d] // y) % d for d in x}
    return {d: (x[d] // y[d]) % d for d in x}
        
class Monkey:
    def __init__(self, items, op, test, all_tests):
        self.items = [mod_dict(i, all_tests) for i in items]
        self.test = monkey_tester(test[0], test[1], test[2])
        self.op = op
    
    def inspect(self):
        item = self.op(self.items[0])
        self.items = self.items[1:]
        # item = mod_div(item, 3)
        to_monk = self.test(item)
        return (to_monk, item)
    
    def add_item(self, item):
        self.items.extend([item])
        
def inspect_full2(monk_list, rounds=20):
    counts = np.zeros(len(monk_list))
    for i in range(rounds):
        monk_list, c = inspect_round2(monk_list)
        counts = counts + c
    
    return monk_list, counts

def inspect_round2(monk_list):
    counts = np.zeros(len(monk_list))
    for i, m in enumerate(monk_list):
        for j in range(len(m.items)):
            to_m, it = m.inspect2()
            monk_list[to_m].add_item(it)
            counts[i] += 1
    return monk_list, counts
            
def main():
    all_tests = [3, 5, 2, 13, 11, 17, 19, 7]
    M = [Monkey([99, 67, 92, 61, 83, 64, 98], op=lambda x: mod_mult(x, 17), test=[3, 4, 2], all_tests=all_tests),
         Monkey([78, 74, 88, 89, 50], op=lambda x: mod_mult(x, 11), test=[5, 3, 5], all_tests=all_tests),
         Monkey([98, 91], op=lambda x: mod_add(x, 4), test=[2, 6, 4], all_tests=all_tests),
         Monkey([59, 72, 94, 91, 79, 88, 94, 51], op=lambda x: mod_mult(x, x), test=[13, 0, 5], all_tests=all_tests),
         Monkey([95, 72, 78], op=lambda x: mod_add(x, 7), test=[11, 7, 6], all_tests=all_tests),
         Monkey([76], op=lambda x: mod_add(x, 8), test=[17, 0, 2], all_tests=all_tests),
         Monkey([69, 60, 53, 89, 71, 88], op=lambda x: mod_add(x, 5), test=[19, 7, 1], all_tests=all_tests),
         Monkey([72, 54, 63, 80], op=lambda x: mod_add(x, 3), test=[7, 1, 3], all_tests=all_tests)]
    M, c = inspect_full(M, rounds=10000)
    c = np.sort(c)
    print(c[-1] * c[-2])
    
    # M = [Monkey([99, 67, 92, 61, 83, 64, 98], op=lambda x: x * 1, test=[3, 4, 2]),
    #      Monkey([78, 74, 88, 89, 50], op=lambda x: x if x % 11 == 0 else x * 11, test=[5, 3, 5]),
    #      Monkey([98, 91], op=lambda x: x + 4, test=[2, 6, 4]),
    #      Monkey([59, 72, 94, 91, 79, 88, 94, 51], op=lambda x: x * 1, test=[13, 0, 5]),
    #      Monkey([95, 72, 78], op=lambda x: x + 7, test=[11, 7, 6]),
    #      Monkey([76], op=lambda x: x + 8, test=[17, 0, 2]),
    #      Monkey([69, 60, 53, 89, 71, 88], op=lambda x: x + 5, test=[19, 7, 1]),
    #      Monkey([72, 54, 63, 80], op=lambda x: x + 3, test=[7, 1, 3])]
    # M, c = inspect_full2(M, rounds=1)
    # print(c)
    # test = [3, 5, 2, 13, 11, 19, 7]
    # ops = [*17, *11, +4, *x, +7, +8, +5, +3]
    
if __name__ == '__main__':
    test_eleven()
    main()