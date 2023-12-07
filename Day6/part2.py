# -*- coding: utf-8 -*-

"""
Day 6: Wait for it
==================

Part 2
--------
https://adventofcode.com/2023/day/6#part2

Module Info
-----------
:Date: 2023-12-06
:Version: 1.0.0
:Authors: - Alexandre CONDETTE <alexandre.condette@wanadoo.fr>
:platform: Unix, Windows, MacOS
"""

#%% Library
import pathlib

#%% Constants and global Variables
dayPath:pathlib.Path = pathlib.Path("./Day6")   # Current Path
#dayPath:pathlib.Path = pathlib.Path(".")   # Current Path
data:list            = list()   # Input Data
time:list = int()
record:list = int()
win: list = int()

runExample:bool = False

answer_i:int = 1

#%% Functions
def getTime(data:str = None) -> int:
    """
    """
    global time
    time = data.split("\nDistance:")[0].split(":")[-1].split(" ")
    time = list(filter(lambda x: x!="", time))
    time = int(''.join(time))

    return time

def getRecord(data:str = None) -> list:
    """
    """
    global record
    record = data.split("Distance:")[-1].split(" ")
    record = list(filter(lambda x: x!="", record))
    record = int(''.join(record))

    return record

def winRaces(time:int = 0, records:int = 0) -> int:
    """
    """
    global answer_i
    nbWins = 0
    for speed in range(time):
        travel = speed * (int(time) - speed)

        if travel > record :
            nbWins +=1
    answer_i = nbWins
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
    global answer_i
    getTime(data)
    getRecord(data)
    winRaces(time, record)

    return answer_i

# %% Output
if __name__ == "__main__" :
    if runExample :
        with open(dayPath / 'example.txt', 'r') as raw_data:
            data = raw_data.read()
    else :
        with open(dayPath / 'input.txt', 'r') as raw_data:
            data = raw_data.read()

    print(answer())