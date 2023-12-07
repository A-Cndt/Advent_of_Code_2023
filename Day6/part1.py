# -*- coding: utf-8 -*-

"""
Day 6: Wait for it
==================

Part 1
--------
https://adventofcode.com/2023/day/6#part1

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
times:list = list()
records:list = list()
wins: list = list()

runExample:bool = False

answer_i:int = 1

#%% Functions
def getTimes(data:str = None) -> list:
    """
    """
    global times
    times = data.split("\nDistance:")[0].split(":")[-1].split(" ")
    times = list(filter(lambda x: x!="", times))


    return times

def getRecords(data:str = None) -> list:
    """
    """
    global records
    records = data.split("Distance:")[-1].split(" ")
    records = list(filter(lambda x: x!="", records))

    return records

def winRaces(times:list = list(), records:list = list) -> list:
    """
    """
    for race in times :
        nbWins = 0
        for speed in range(0, int(race)):
            travel = speed * (int(race) - speed)
            index = times.index(race)
            if travel > int(records[index]) :
                nbWins +=1
        wins.append(nbWins)

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
    getTimes(data)
    getRecords(data)
    winRaces(times, records)
    for win in wins:
        answer_i *= win
    # answer =
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