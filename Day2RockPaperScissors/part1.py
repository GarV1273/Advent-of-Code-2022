#!/usr/bin/env python3
# Author: Gavin Sutherland
# Date of Creation: 12/2/2022
# File Name: part1.py
# Purpose: main script for advent of code day 2 part 1

'''The goal: Take the two characters in each line to calculate a score, then sum up that score'''

# This is the dict of point assignments. The user move (x, y, or z) will be entered. The dict will return the points
choice_points = {
    'x': 1,
    'y': 2,
    'z': 3
}

# These are the point based on the round. x/a, y/b, and z/c are rock/paper/scissors. You can retrieve the round points through a 2d index
# duel_points[your_move][opponent_move] should return the correct points
duel_points = {
    'x': {
        'a': 3,
        'b': 0,
        'c': 6
    },

    'y': {
        'a': 6,
        'b': 3,
        'c': 0
    },

    'z': {
        'a': 0,
        'b': 6,
        'c': 3
    }
}

score = 0

# Process data
with open('data.txt') as f:
    rps_data = f.readlines()

# Data processing
for round in rps_data:
    opponent_move = round[0].lower()
    your_move = round[2].lower()
    
    score += choice_points[your_move] + duel_points[your_move][opponent_move]

print(score)