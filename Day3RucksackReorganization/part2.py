#!/usr/bin/env python3
# Author: Gavin Sutherland
# Date of Creation: 12/3/2022
# File Name: part1.py
# Purpose: main script for advent of code day 3 part 1

'''
The goal: Find the common character in three strings, convert it to a number, and sum all of them up

The plan:
- Get data from file
- Loop through  every line
- You need to do data processing every third line. Store each line in a list, and when the list is three items long, do the processing
- Find the intersection of the strings using set()
- Convert to a number
- Add to sum

- Final result should be the sum of all those numbers
'''

sum = 0
# The group we are currently processing. It will be used once it is three items long, then it will be emptied
current_group = []

with open('data.txt', 'r') as f:
    sacks = f.readlines()

for sack in sacks:
    # Removed the newline chars. It didn't cause a problem last time so idk. Probably better practice
    sack = sack.replace("\n", "")
    current_group.append(sack)

    # Skips if there isn't three in the group yet
    if len(current_group) != 3: continue
    
    # This line finds the common_letter. You can convert all strings to sets, and using the & operator, it will only return items that are in every set.
    # We can grab the result by converting the new set to a list and grabing the first (and only) index.
    common_letter = list(set(current_group[0]) & set(current_group[1]) & set(current_group[2]))[0]
    print(f"common letter: {common_letter}")

    # I use ord() to convert the number to a letter. Need to check if it is upper or lower first, as that determines the decimal code and thus the math
    if common_letter.isupper():
        sum += ord(common_letter) - 38
        print(f"adding {ord(common_letter) - 38}")
    else:
        sum += ord(common_letter) - 96
        print(f"adding {ord(common_letter) - 96}")

    # Reset the group
    current_group = []
    
    print(f"{sum}\n")

print(sum)