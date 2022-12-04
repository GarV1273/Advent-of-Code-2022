#!/usr/bin/env python3
# Author: Gavin Sutherland
# Date of Creation: 12/4/2022
# File Name: part1.py
# Purpose: main script for advent of code day 4 part 1

'''
The goal: Check if one list fully contains another and sum up the number of pairs where they do

The plan:
- Get data from file
- Loop through  every line
- Remove the newline characters
- Turn each range into a set
- Do set subtraction and test for an empty set
- If the set is empty, it means that the contents of one set were entirely in another set, so we add to the total

- Final result should be the sum of all the pairs where one fully contains another
'''

total = 0

with open('data.txt', 'r') as f:
    pairs = f.readlines()

for pair in pairs:
    pair = pair.replace("\n", "")

    # Splits into the two elves
    pair = pair.split(",")

    # Splits the two numbers into a list to use for the range
    pair[0] = pair[0].split("-")
    pair[1] = pair[1].split("-")

    print(f"Pair: {pair}")
    
    # Grab the start and end of the groups and return it as a list
    elf1_groups = range(int(pair[0][0]), int(pair[0][1])+1)
    elf2_groups = range(int(pair[1][0]), int(pair[1][1])+1)

    # A property of sets in python is that an empty one will always return false if tested in a condition
    # If you subtract a set from another, you will get the items in the first set that aren't in the second set, but if all the items in set 1 are in set 2, it will return an empty set
    # Using these two properties, we can test if the subtraction of the sets results in an empty list, and thus, one list entirely containing another. If they do not, skip it

    if set(elf1_groups) - set(elf2_groups) and set(elf2_groups) - set(elf1_groups):
        print("Both sets contain unique items\n")
        continue

    print("One list fully contains the other\n")

    total += 1

print(f"Final resutl: {total}")