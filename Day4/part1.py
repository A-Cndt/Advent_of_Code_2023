# -*- coding: utf-8 -*-

"""
Day 4: ScratchCards
===================

Part 1
--------
https://adventofcode.com/2023/day/4#part1

Module Info
-----------
:Date: 2023-12-<DAY>
:Version: 1.0.0
:Authors: - Alexandre CONDETTE <alexandre.condette@wanadoo.fr>
:platform: Unix, Windows, MacOS
"""

#%% Library
import pathlib
import re

#%% Constants and global Variables
dayPath:pathlib.Path = pathlib.Path("./Day4")   # Current Path

data:list            = list()   # Input Data

runExample:bool = False

answer_i:int = 0
match = 0

#%% Functions
def getWinningNumbers(line:str = None):
    """
    """
    winningNumbers = line.split("|")[0].split(":")[-1]
    winningNumbers = re.findall("\d+", winningNumbers)

    return winningNumbers
def getNumberYouHave(line:str = None):
    """
    """
    myNumbers = line.split("|")[-1]
    myNumbers = re.findall("\d+", myNumbers)

    return myNumbers
def numberOfMatch(winningNumbers, myNumbers):
    match = 0
    for number in myNumbers:
        if number in winningNumbers:
            match += 1
    return match

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
    for line in data:
        w=getWinningNumbers(line)
        m=getNumberYouHave(line)
        match = numberOfMatch(w,m)
    # answer =
        if match > 0 :
            answer_i += 2 ** (match - 1)
    return answer_i

# %% Output
if __name__ == "__main__" :
    if runExample :
        with open(dayPath / 'example.txt', 'r') as raw_data:
            data = raw_data.readlines()
    else :
        with open(dayPath / 'input.txt', 'r') as raw_data:
            data = raw_data.readlines()

    print(answer())