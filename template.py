# -*- coding: utf-8 -*-

"""
Day <DAY>: <NAME>
==================

Part <PART>
--------
https://adventofcode.com/2023/day/<DAY>#part<PART>

Module Info
-----------
:Date: 2023-12-<DAY>
:Version: 1.0.0
:Authors: - Alexandre CONDETTE <alexandre.condette@wanadoo.fr>
:platform: Unix, Windows, MacOS
"""

#%% Library
import pathlib

#%% Constants and global Variables
dayPath:pathlib.Path = pathlib.Path("./Day<DAY>")   # Current Path

data:list            = list()   # Input Data

runExample:bool = True

answer:int = 0

#%% Functions


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
    for line in data:
        pass

    # answer =
    return answer

# %% Output
if __name__ == "__main__" :
    if runExample :
        with open(dayPath / 'example.txt', 'r') as raw_data:
            data = raw_data.readlines()
    else :
        with open(dayPath / 'input.txt', 'r') as raw_data:
            data = raw_data.readlines()

    print(answer())