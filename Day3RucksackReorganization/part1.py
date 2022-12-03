#!/usr/bin/env python3
# Author: Gavin Sutherland
# Date of Creation: 12/3/2022
# File Name: part1.py
# Purpose: main script for advent of code day 3 part 1

'''
The goal: Find the common item in two lists of characters, convert it to a number, and sum all of them up

The plan:
- Get data from file
- Loop through  every line
- Remove the newline characters
- Divide string into two lists representing half of the bag
- Find the intersection of the lists using set()
- Convert to a number
- Add to sum

- Final result should be the sum of all those numbers
'''

sum = 0

with open('data.txt', 'r') as f:
    sacks = f.readlines()

print(sacks)

for sack in sacks:
    # I use string slicing to split the string in half
    first_half = sack[0:int(len(sack)/2)]
    second_half = sack[int(len(sack)/2):]
    
    # This line finds the common_letter. You can convert both strings to sets, and using the & operator, it will only return items that are in both lists.
    # We can grab the result by converting the new set to a list and grabing the first (and only) index.
    common_letter = list(set(first_half) & set(second_half))[0]
    print(f"common letter: {common_letter}")

    # I use ord() to convert the number to a letter. Need to check if it is upper or lower first, as that determines the decimal code and thus the math
    if common_letter.isupper():
        sum += ord(common_letter) - 38
        print(f"adding {ord(common_letter) - 38}")
    else:
        sum += ord(common_letter) - 96
        print(f"adding {ord(common_letter) - 96}")
    
    print(f"{sum}\n")

print(sum)