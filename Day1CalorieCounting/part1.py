#!/usr/bin/env python3
# Author: Gavin Sutherland
# Date of Creation: 12/1/2022
# File Name: part1.py
# Purpose: main script for advent of code day 1 part 1

'''The goal: Find the highest sum of stacked numbers in a text file'''

# Process data
with open('data.txt') as f:
    calorie_data = f.readlines()

# Variables
current_sum = 0 # keeps track of the current total to be appeded when a line skip is reached
processed_calorie_data = [] # The list of the summed calories of each elf
most_calories = 0

# Data processing
for calorie in calorie_data:
    if calorie == "\n": # The end of an elf's inventory
        processed_calorie_data.append(current_sum)
        current_sum = 0
    else:
        current_sum += int(calorie.replace("\n", "")) # Data is writen as "number\n", so we need to remove the newline character and make it a number for later processing

processed_calorie_data.append(current_sum) # This line ensures the final sum is added to the list, as there is no newline character at the end of the file

most_calories = sorted(processed_calorie_data)[-1] # Sort the list numerically and get the last value. This should be the max of the list

print(f"Most calories: {most_calories}")