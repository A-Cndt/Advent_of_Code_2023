# -*- coding: utf-8 -*-

"""
Day 3: Gear Ratios
==================

Part 1
--------
https://adventofcode.com/2023/day/3

Module Info
-----------
:Date: 2023-12-03
:Version: 1.0.0
:Authors: - Alexandre CONDETTE <alexandre.condette@wanadoo.fr>
:platform: Unix, Windows, MacOS
"""

#%% Library
import pathlib
import re
#%% Constants and global Variables
dayPath:pathlib.Path = pathlib.Path("./Day3")   # Current Path

data:list            = list()   # Input Data

runExample:bool = False

answer_i:int = 0

#%% Functions
def paddedInput(data:str = None):
    """
    """
    width:int = len(data[0])

    output = [
            "." * (width + 2),
            *[f".{l}." for l in data],
            "." * (width + 2),
            ]
    return output

def get_directions(x_offset, y_offset):
    for y in range(-1, 2):
        for x in range(-1, 2):
            yield x + x_offset, y + y_offset

# %% Answer

def answer():
    """
    answer
    ======

    Solve the current Day part 1

    :param: None
    :return: answer
    :rtype: int

    """
    valid_map = [[0 for _ in range(len(data[0]))] for _ in range(len(data))]

    for i, row in enumerate(data[1:-1]):
        for j, char in enumerate(row[1:-1]):
            if not (char == "." or char.isnumeric()):
                for x, y in get_directions(j + 1, i + 1):
                    valid_map[y][x] = 1

    current_number = '0'
    num_valid = False
    sm = 0

    for i, row in enumerate(data):
        for j, char in enumerate(row):
            if char.isnumeric():
                num_valid = num_valid or valid_map[i][j]
                current_number += char
            else:
                if num_valid:
                    sm += int(current_number)
                num_valid = False
                current_number = '0'

    return(sm)

# %% Output
if __name__ == "__main__" :
    if runExample :
        with open(dayPath / 'example.txt', 'r') as raw_data:
            data = raw_data.readlines()
    else :
        with open(dayPath / 'input.txt', 'r') as raw_data:
            data = raw_data.readlines()

    print(answer())