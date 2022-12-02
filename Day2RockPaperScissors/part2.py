#!/usr/bin/env python3
# Author: Gavin Sutherland
# Date of Creation: 12/2/2022
# File Name: part2.py
# Purpose: main script for advent of code day 2 part 2

'''The goal: Take the two characters in each line to calculate a score, then sum up that score

This time, the second column is if we need to lose(x), draw(y), or win(z)

The plan:
Grab the opponents move and the game ending
The game ending can be easily converted into points, as x = 0, y=3, and z = 6
To find the choice, we need to take the opponent move and go up or down 1 move depending on the win condition
'''

# This is the dict of point assignments. The user move (x, y, or z) will be entered. The dict will return the points
choice_points = {
    'rock': 1,
    'paper': 2,
    'scissors': 3
}

# These are the point based on the end state of the round. This time, they are determined by the second column of letters
duel_points = {
    'x': 0,
    'y': 3,
    'z': 6
}

your_move = {
    'x': {
        'a': 'scissors',
        'b': 'rock',
        'c': 'paper'
    },
    'y': {
        'a': 'rock',
        'b': 'paper',
        'c': 'scissors'
    },
    'z': {
        'a': 'paper',
        'b': 'scissors',
        'c': 'rock'
    }
}

score = 0

# Process data
with open('data.txt') as f:
    rps_data = f.readlines()

# Data processing
for round in rps_data:
    opponent_move = round[0].lower()
    game_result = round[2].lower()

    score += duel_points[game_result] + choice_points[your_move[game_result][opponent_move]]


    

print(score)