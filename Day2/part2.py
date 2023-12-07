# -*- coding: utf-8 -*-

"""
Day 2: Cube Conundrum
==================

Part 2
--------
https://adventofcode.com/2023/day/2#part2

Module Info
-----------
:Date: 2023-12-02
:Version: 1.0.0
:Authors: - Alexandre CONDETTE <alexandre.condette@wanadoo.fr>
:platform: Unix, Windows, MacOS
"""

#%% Library
import pathlib
import re

#%% Constants and global Variables
dayPath:pathlib.Path = pathlib.Path("./Day2")   # Current Path

data:list            = list()   # Input Data

runExample:bool   = False

redCubes:int   = 0
greenCubes:int = 0
blueCubes:int  = 0

answer_i:int = 0


#%% Functions
def splitGame(line:str = None):
    """
    splitGame
    =========
    Get all the subgames in a Game

    :param line: The current line of data to check
    :type line: str
    :return: gamesList, a list of all the subGames
    :rtype: list

    """
    gamesList:list = line.split(":")[-1].split(";")
    return gamesList

def countRed(line:str = None):
    """
    countRed
    ========
    Count all the red cubes in a Game and get the minimum number of them for the game to be possible

    :param line: The current line of data to check
    :type line: str
    :return: redCubes, min nb of red cubes for the game to be possible
    :rtype: int
    """
    global redCubes
    try :
        nbRed:int = int(re.findall('(\d+) red', line)[-1])
    except:
        nbRed:int = 0

    if nbRed > redCubes :
        redCubes = nbRed
    else :
        pass

    return redCubes

def countGreen(line:str = None):
    """
    countGreen
    ==========
    Count all the green cubes in a Game and get the minimum number of them for the game to be possible

    :param line: The current line of data to check
    :type line: str
    :return: greenCubes, min nb of green cubes for the game to be possible
    :rtype: int

    """
    global greenOK, greenCubes
    try :
        nbGreen:int = int(re.findall('(\d+) green', line)[-1])
    except:
        nbGreen:int = 0

    if nbGreen > greenCubes :
        greenCubes = nbGreen
    else :
        pass

    return greenCubes

def countBlue(line:str = None):
    """
    countBlue
    =========
    Count all the blue cubes in a Game and get the minimum number of them for the game to be possible

    :param line: The current line of data to check
    :type line: str
    :return: blueCubes, min nb of blue cubes for the game to be possible
    :rtype: int

    """
    global blueOK, blueCubes
    try :
        nbBlue:int = int(re.findall('(\d+) blue', line)[-1])
    except:
        nbBlue:int = 0

    if nbBlue > blueCubes :
        blueCubes = nbBlue
    else :
        pass

    return blueCubes

def isGamePossible(gamesList:list = list()):
    """
    isGamePossible
    ==============
    Get for each game the minimal value of each type of cubes
    :param gamesList: List of the subgames of a game
    :type gamesList: list
    :return: cubesNb, a tuple of nb of cubes (red, green, blue)
    :rtype: tuple

    """

    global blueCubes, greenCubes, redCubes
    blueCubes = 0
    redCubes = 0
    greenCubes = 0

    for game in gamesList:

        reds:int = countRed(game)
        greens:int = countGreen(game)
        blues:int = countBlue(game)

    cubesNb:tuple = (reds, greens, blues)
    return cubesNb

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
        gamesList:list = splitGame(line)
        cubesNb:tuple = isGamePossible(gamesList)
        answer_i += cubesNb[0] * cubesNb[1] * cubesNb[2]

    # answer =
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