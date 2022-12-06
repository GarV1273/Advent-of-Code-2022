#!/usr/bin/env python3
# Author: Gavin Sutherland
# Date of Creation: 12/5/2022
# File Name: part1.py
# Purpose: main script for advent of code day 6 part 1

'''
The goal: Move boxes based on the given instructions and return the top boxes

The plan:
- Get data from file. This will be a string variable.
- Loop through the list
- Each iteration, slice the list starting at the current index and ending at the current index + 4
- If there are matching characters, return the index
'''

class Main(object):
    '''Main class for part 1'''
    def __init__(self, filename) -> None:
        self.data = self.preprocess_data(filename)
        self.start_of_packet = self.process_data()

    def preprocess_data(self, filename):
        '''Takes a text file and returns the contents as a string'''
        with open(filename, 'r') as f:
            return f.readline()
        
    def process_data(self):
        for i in range(int(len(self.data) - 4)):
            current_slice = self.data[i:i+4]
            for j in current_slice:
                print(current_slice)
                if len(list(current_slice)) == len(set(list(current_slice))):
                    return i + 4

if __name__ == '__main__':
    main = Main('data.txt')
    print(main.start_of_packet)