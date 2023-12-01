# -*- coding: utf-8 -*-

"""
Day 1: Trebuchet?!
==================

Part Two
--------
https://adventofcode.com/2023/day/1#part2

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
import sys

#%% Constants and global Variables
dayPath:pathlib.Path = pathlib.Path("./Day1")   # Current Path

data:list            = list()   # Input Data
digits:list          = list()   # List of all the digit

spelledDigits:dict   = {"one":1, "two":2, "three":3, "four":4, "five": 5, "six":6, "seven":7, "eight":8, "nine":9}

unit:int             = 0        # Last Digit
ten:int              = 0        # First Digit

runExample:bool      = False     # If we want to run the example given by AoC

#%% Functions
def checkSpelledDigit(line:str = None):
    """
    checkSpelledDigit
    =================
    Read the line and get the index of spelled digits
    This function does also check if the digit is repeated in the string and get all its indexes

    :param line: The current line of the input file to look at
    :type line: str
    :return: spelledDigitList > List of spelled digits values and their index
    :rtype: list
    """
    spelledDigitsList:list = list()
    for key, value in spelledDigits.items():
        if key in line :
            indexes = re.finditer(key, line)
            for index in indexes:
                spelledDigitsList.append((value, index.start()))

    return spelledDigitsList

def checkNumericDigit(line:str = None):
    """
    checkNumericDigit
    =================
    Read the line and get the index of numerical digits
    This function does also check if the digit is repeated in the string and get all its indexes

    :param line: The current line of the input file to look at
    :type line: str
    :return: numericDigitList > List of numerical digits values and their index
    :rtype: list
    """
    numericDigitsList:list = list()
    lineDigits:list = re.findall(r'\d', line)

    for digit in lineDigits:
        indexes = re.finditer(digit, line)
        for index in indexes:
            numericDigitsList.append((int(digit), index.start()))

    return numericDigitsList

def extractFirstDigit(allDigits:list = list()):
    """
    extractFirstDigit
    =================
    Get the first digit that appear in a string and return it, it compare the indexes of numericDigits and spelledDigits and get the value with the lowest index

    :param line: The current line of the input file to look at
    :type line: str
    :return: firstDigit > Value of the 1st digit in the line (spelled of numerical)
    :rtype: int
    """
    firstDigit = min(allDigits, key=lambda tup: tup[1])[0]
    return firstDigit

def extractLastDigit(allDigits:list = list()):
    """
    extractLastDigit
    =================
    Get the last digit that appear in a string and return it, it compare the indexes of numericDigits and spelledDigits and get the value with the highest index

    :param line: The current line of the input file to look at
    :type line: str
    :return: lastDigit
    :rtype: int
    """
    lastDigit = max(allDigits, key=lambda tup: tup[1])[0]
    return lastDigit

# %% Answer
def answer():
    """
    answer
    ======

    Solve the current Day part 2

    :param: None
    :return: answer
    :rtype: int
    """
    for line in data:
        # Get the value
        spelledDigitsList:list = checkSpelledDigit(line)
        numericDigitsList:list = checkNumericDigit(line)
        allDigits:list = spelledDigitsList + numericDigitsList

        ten:int  = extractFirstDigit(allDigits)
        unit:int = extractLastDigit(allDigits)

        # Make a 2 digit number
        digits.append(int(str(ten) + str(unit)))

        # Answer = Sum(digits)
    answer:int = sum(digits)
    return answer

# %% Output
if __name__ == "__main__" :
    #%% Open Input datas
    if runExample :
        with open(dayPath / 'example.txt', 'r') as raw_data:
            data = raw_data.readlines()
    else :
        with open(dayPath / 'input.txt', 'r') as raw_data:
            data = raw_data.readlines()

    print(answer())
