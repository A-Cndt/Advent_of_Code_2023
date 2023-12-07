# -*- coding: utf-8 -*-

"""
Day 3: Gear Ratios
==================

Part 2
--------
https://adventofcode.com/2023/day/3#part2

Module Info
-----------
:Date: 2023-12-03
:Version: 1.0.0
:Authors: - Alexandre CONDETTE <alexandre.condette@wanadoo.fr>
:platform: Unix, Windows, MacOS
"""

#%% Library
import pathlib

#%% Constants and global Variables
dayPath:pathlib.Path = pathlib.Path("./Day3")   # Current Path

data:list = list()   # Input Data

runExample:bool = False

answer_i:int = 0

#%% Functions

def get_directions(x_offset, y_offset):
    for y in range(-1, 2):
        for x in range(-1, 2):
            yield x + x_offset, y + y_offset

def h_flood(x: int, y: int, m: int) -> str:
    if not data[y][x].isnumeric():
        return ""
    flood = h_flood(x + m, y, m)
    return f'{flood if m < 0 else ""}{data[y][x]}{flood if m > 0 else ""}'

def get_surrounding(x: int, y: int) -> list:
    return list(map(int, filter(lambda _: _,
                                {h_flood(_x, _y, -1)[:-1] + h_flood(_x, _y, 1) for _x, _y in get_directions(x, y) if
                                 data[_y][_x] != '*'})))

# %% Answer

def answer():
    """
    answer
    ======

    Solve the current Day part <PART>

    :param: None
    :return: answer
    :rtype: int

    """
    total = 0
    global data

    for i, row in enumerate(data):
        for j, char in enumerate(row):
            if char == '*':
                if len(get_surrounding(j, i)) == 2:
                    nums = get_surrounding(j,i)
                    total += nums[0] * nums[1]

    # answer =
    return total

# %% Output
if __name__ == "__main__" :
    if runExample :
        with open(dayPath / 'example.txt', 'r') as raw_data:
            data = raw_data.readlines()
    else :
        with open(dayPath / 'input.txt', 'r') as raw_data:
            data = raw_data.readlines()

    print(answer())