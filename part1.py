# -*- coding: utf-8 -*-

"""
Day 1: Trebuchet?!
==================

Part One
--------
https://adventofcode.com/2023/day/1#part1

Module Info
-----------
:Date: 2023-12-01
:Version: 1.0.0
:Authors: - Alexandre CONDETTE <alexandre.condette@wanadoo.fr>
:platform: Unix, Windows, MacOS
"""
#%% Library
import pathlib
import re

#%% Constants and global Variables
dayPath:pathlib.Path = pathlib.Path("./Day1")   # Current Path

data:list            = list()   # Input Data
digits:list          = list()   # List of all the digit

unit:int             = 0        # Last Digit
ten:int              = 0        #First Digit

runExample:bool      = False     # If we want to run the example given by AoC

#%% Open Input datas
if runExample :
    with open(dayPath / 'example_p1.txt', 'r') as raw_data:
        data = raw_data.readlines()
else :
    with open(dayPath / 'input.txt', 'r') as raw_data:
        data = raw_data.readlines()

#%% Functions
def extractFirstDigit(line:str = None):
    """
    extractFirstDigit
    =================
    Get the first digit that appear in a string and return it

    :param line: The current line of the input file to look at
    :type line: str
    :return: firstDigit
    :rtype: int
    """
    lineDigits:list = re.findall(r'\d', line)
    firstDigit:int  = lineDigits[0]

    return firstDigit

def extractLastDigit(line:str = None):
    """
    extractLastDigit
    =================
    Get the last digit that appear in a string and return it

    :param line: The current line of the input file to look at
    :type line: str
    :return: lastDigit
    :rtype: int
    """
    lineDigits:list = re.findall(r'\d', line)
    lastDigit:int   = lineDigits[-1]

    return lastDigit

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
    for line in data:
        # Get the value
        ten:int  = extractFirstDigit(line)
        unit:int = extractLastDigit(line)

        # Make a 2 digit number
        digits.append(int(str(ten) + str(unit)))

        # Answer = Sum(digits)
    answer:int = sum(digits)
    return answer

# %% Output
if __name__ == "__main__" :
    print(answer())