# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 10:50:58 2022

@author: taiki.sakai
Day 2!
"""
#%% data loading
f = open('data/input02.txt', 'r')
data = f.readlines()
f.close()
#%% processing
pairs = [[x[0], x[2]] for x in data]
# A, X ROCK = 1pt
# B, Y PAPER = 2pt
# C, Z SCISS = 3pt
# Loss, Draw, WIn = 0, 3, 6 pt

#%% score a round

def score_one_rps(x):
    score = 0 
    match x[1]:
        case 'X':
            score +=1
            match x[0]:
                case 'A':
                    score += 3
                case 'B':
                    score += 0
                case 'C':
                    score += 6
        case 'Y':
            score +=2
            match x[0]:
                case 'A':
                    score += 6
                case 'B':
                    score += 3
                case 'C':
                    score += 0
        case 'Z':
            score +=3
            match x[0]:
                case 'A':
                    score += 0
                case 'B':
                    score += 6
                case 'C':
                    score += 3           
    return score
#%%%
scores = [score_one_rps(x) for x in pairs]
sum(scores)
#%% Part 2
# X lose Y Draw Z win. ABC XYZ RPS
def map_to_play(x):
    match x[0]:
        case 'A':
            match x[1]:
                case 'X':
                    x[1] = 'Z'
                case 'Y':
                    x[1] = 'X'
                case 'Z':
                    x[1] = 'Y'
        case 'B':
            match x[1]:
                case 'X':
                    x[1] = 'X'
                case 'Y':
                    x[1] = 'Y'
                case 'Z':
                    x[1] = 'Z'
        case 'C':
            match x[1]:
                case 'X':
                    x[1] = 'Y'
                case 'Y':
                    x[1] = 'Z'
                case 'Z':
                    x[1] = 'X'
    return x
#%%
score_one_rps(map_to_play(['C', 'Z']))
#%%
new_pairs = [map_to_play(x) for x in pairs]
scores = [score_one_rps(x) for x in new_pairs]
sum(scores)