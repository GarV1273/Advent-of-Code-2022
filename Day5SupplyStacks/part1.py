#!/usr/bin/env python3
# Author: Gavin Sutherland
# Date of Creation: 12/5/2022
# File Name: part1.py
# Purpose: main script for advent of code day 5 part 1

'''
The goal: Move boxes based on the given instructions and return the top boxes

This would be best done with list processing
'''

with open('data.txt', 'r') as f:
    data = f.readlines()

# Creates one list for each stack
stacks = [[] for i in range(int(len(data[0])/4))]

# This section processes the box data
for line in data:
    # End processing when we reach the end of the boxes
    if line[1] == "1": 
        break

    # Similar to a js loop. Starts at 1 and only tests every 4th character. SHould be more efficient than testing everything
    for i in range(1, int(len(data[0])), 4):
        if line[i] not in [' ', '[', ']']: # Blacklist
            stacks[i // 4].append(line[i]) # i //4 should return the relative index, as we are procesing every 4th character

print(stacks)

# This section does the actual moving
for line in data:
    # Skips the lines w/o a move command
    if line[0] != 'm': continue

    commands = line.split(" ") #['move', '#', 'from', '#', 'to', '#']
    # Should repeat the moving processes based on the move command
    for i in range(int(commands[1])):
        # This takes the stack from the 'from' command, removes the fist item, and inserts it to the 'to' command list
        stacks[int(commands[5])-1].insert(0, stacks[int(commands[3])-1].pop(0))

print(stacks)

for stack in stacks:
    print(stack[0], end='')