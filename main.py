# -*- coding: utf-8 -*-
"""
main.py
=======
"""

#%% Code Infos
__author__     = "Alexandre Condette"
__copyright__  = "Copyright 2023, AoC 2023 Project"
__credits__    = "Alexandre Condette"
__licence__    = "MIT"
__version__    = "1.0.0"
__maintainer__ = "Alexandre Condette"
__email__      = "alexandre.condette@protonmail.com"
__status__     = "Production"
__docformat__  = "reStructuredText"

#%% Libray Imports
import os
import subprocess
import datetime
import numpy
import textwrap
import shutil
import pathlib

#%% Constants and global variables
date:datetime.date = datetime.date.today()
day:int = int(date.strftime('%d'))
days:list = numpy.arange(1, day+1, 1)
#%% runDay
def runDay(day:int = day, part:str = "a"):
    """
    """

    date:datetime.date = datetime.date(2023,12,day)

    print(f"Results of the day: \33[1;49;34m{date}\33[0;m")
    print("------------------------------")

    if part == "1" or part == "a":
        answer_1 = subprocess.check_output(f"python ./Day{day}/part1.py", shell=True).decode()
        print(f"\33[38;5;11mPart 1:\33[0;m {answer_1}")

    if part == "2" or part == "a" :
        answer_2 = subprocess.check_output(f"python ./Day{day}/part2.py", shell=True).decode()
        print(f"\33[38;5;11mPart 2:\33[0;m {answer_2}")

    return 0

#%% makeDay
def makeDay():
    """
    """
    os.mkdir(f"./Day{day}")

    pathlib.Path(f"./Day{day}/example.txt").touch()
    pathlib.Path(f"./Day{day}/input.txt").touch()

    shutil.copy("template.py", f"./Day{day}/part1.py")
    shutil.copy("template.py", f"./Day{day}/part2.py")

    return 0

#%% Main
if __name__ == "__main__" :
    os.system('cls')

    # Check Current Date
    introMsg:str = textwrap.dedent(f'''
                               \033[1;32m
                               +==========================+
                               |                          |
                               |   \033[38;5;11mAdvent Of Code 2023\033[1;32m    |
                               |   *\033[1;31m*\033[1;32m*\033[1;31m*\033[1;32m*\033[1;31m*\033[1;32m*\033[1;31m*\033[1;32m*\033[1;31m*\033[1;32m*\033[1;31m*\033[1;32m*\033[1;31m*\033[1;32m*\033[1;31m*\033[1;32m*\033[1;31m*\033[1;32m*    |
                               |                          |
                               +==========================+
                               \033[0;m

                               Made by: {__author__}
                               Current version: {__version__}
                               (c) {__copyright__}

                               - Current Date: {date}
                               - Available Days: {days}

          ''')

    print(introMsg)

    # Check if current day repository exist
    if not os.path.isdir(f"./Day{day}"):
        print("Current Day repository does not exist")
        ans = input("Do you want to create it ? [y/n] > ")
        if ans.lower() == "y":
            makeDay()
    else:
        runDay()

    runADay:str = input("Do you want to run a specific day? [y/n] > ")

    if runADay.lower() == "y" :
        dayChoice:str = input(f"Choose day number [1:{day}] > ")
        partChoice:str = input("Chose the part to display [1/2/a] (a is for all parts) > ")
        print("\n")
        runDay(int(dayChoice), str(partChoice))
