#!/usr/bin/env python3
# Author: Gavin Sutherland
# Date of Creation: 12/5/2022
# File Name: part1.py
# Purpose: main script for advent of code day 6 part 2

'''
The goal: Move boxes based on the given instructions and return the top boxes

The plan:
- This is exactly like part 1, except for 14 positions except 4. 
- This requires no logic changes, only changing a couple of numbers
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
        for i in range(int(len(self.data) - 14)):
            current_slice = self.data[i:i+14]
            for j in current_slice:
                print(current_slice)
                if len(list(current_slice)) == len(set(list(current_slice))):
                    return i + 14

if __name__ == '__main__':
    main = Main('data.txt')
    print(main.start_of_packet)