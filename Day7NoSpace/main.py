#!/usr/bin/env python3
# Author: Gavin Sutherland
# Date of Creation: 12/5/2022
# File Name: main.py
# Purpose: main script for advent of code day 7 part 1

'''
This one is gonna be a doosey

The goal: Find the directories that are under a certain file size

The plan:
This method is probably hugely ineficient, but I just wwant to get a working solution. I can optimize later (and by optimize I mean either rewrite completely or never come back to it)
- Create a directory object that has a list of contents and a method that returns the combined size of those contents
- Create a file object that has a size property and a method that returns this property
- For the combined size method, it should loop through the contents of the directory by running the getSize method
    - When the method is used on the file, it should return the size
    - When run on a directory, that directory will also loop through it's contents until all the loops close
    - This is similar to recursion, but the method is run on near-identical objects rather than the same method again

- 

Some notes about the data itself:
- A directory will never be listed twice
- For the direcroty contents, the line will be listed as cd x, ls and the contents with x being the directory name
'''

