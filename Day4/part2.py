#!/usr/bin/env python3
# Author: Gavin Sutherland
# Date of Creation: 12/4/2022
# File Name: part2.py
# Purpose: main script for advent of code day 4 part 2

'''
The goal: Check if one list has any intersection with another and return the number that do

The plan: (similar logic to day 3 with set intersection)
- Get data from file
- Loop through  every line
- Remove the newline characters
- Turn each range into a set
- Do set intersection to test for matches
- If the set has values, it means that there wera matching numbers, so we add to the total

- Final result should be the sum of all the pairs with a matching number
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

    # Like day 3, you casn use the & operand with sets to check for intersection
    if set(elf1_groups) & set(elf2_groups):
        print("Matching number\n")
        total += 1
        continue

    print("No matches\n")

print(f"Final resutl: {total}")