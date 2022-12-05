#!/usr/bin/env python3
# Author: Gavin Sutherland
# Date of Creation: 12/5/2022
# File Name: part1.py
# Purpose: main script for advent of code day 5 part 1

'''
The goal: Move boxes based on the given instructions and return the top boxes

This would be best done with list processing

The plan:
- Get data from file
- Loop through every line
- Remove the newline characters
- Turn each range into a set
- Do set subtraction and test for an empty set
- If the set is empty, it means that the contents of one set were entirely in another set, so we add to the total

- Final result should be the sum of all the pairs where one fully contains another
'''

with open('test_data.txt', 'r') as f:
    data = f.readlines()

print(data)