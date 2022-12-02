#!/usr/bin/env python3
# Author: Gavin Sutherland
# Date of Creation: 12/1/2022
# File Name: part2.py
# Purpose: main script for advent of code day 1 part 2

'''The goal: Find the 3 highest sums of stacked numbers in a text file, then add them up'''

# Process data
with open("data.txt", 'r') as f:
    calorie_data = f.readlines()

# Variables
current_sum = 0 # keeps track of the current total to be appeded when a line skip is reached
processed_calorie_data = [] # The list of the summed calories of each elf
top3_calories_sum = 0

# Data processing
# The process is identical to the previous problem Comments have been left in for convinience
for calorie in calorie_data:
    if calorie == "\n": # The end of an elf's inventory
        processed_calorie_data.append(current_sum)
        current_sum = 0
    else:
        current_sum += int(calorie.replace("\n", "")) # Data is writen as "number\n", so we need to remove the newline character and make it a number for later processing

processed_calorie_data.append(current_sum) # This line ensures the final sum is added to the list, as there is no newline character at the end of the file

top3_calories_sum = sum(sorted(processed_calorie_data)[-3::]) # Sort the list numerically and get the last three values. These are the highest three


print(f"Sum of top 3: {top3_calories_sum}")