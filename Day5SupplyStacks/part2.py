#!/usr/bin/env python3
# Author: Gavin Sutherland
# Date of Creation: 12/5/2022
# File Name: part1.py
# Purpose: main script for advent of code day 5 part 2

'''
The goal: Move boxes based on the given instructions and return the top boxes

Instead of using the looping .pop() method of part 1, we need to remove splices of a list and add them to another

- Get the number of boxes to be moves
- Slice a new list starting from the beginning and ending at the 'move' number - 1
- Overwrite the destination list with the new slice + the old destination list
- Use del to delete the slice from the old source
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
    
    # Gets the source and destination lists. Considered one lining, but this is easier to read
    source_list_index = int(commands[3])-1
    dest_list_index = int(commands[5])-1

    # Construct the new list
    print(f"Stacks before change: {stacks}")
    stacks[dest_list_index] = stacks[source_list_index][:int(commands[1])] + stacks[dest_list_index]
    print(f"Stacks after moving: {stacks}")
    
    # Remove the moved items from the old list
    del stacks[source_list_index][:int(commands[1])]
    print(f"Stacks after deletion: {stacks}\n")

print(stacks)

for stack in stacks:
    if stack:
        print(stack[0], end='')