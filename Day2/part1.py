# -*- coding: utf-8 -*-

"""
Day 2: Cube Conundrum
==================

Part 1
--------
https://adventofcode.com/2023/day/2#part1

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
gamePossible:bool = True
redOK:bool        = True
greenOK:bool      = True
blueOK:bool       = True

redCubes:int   = 12
greenCubes:int = 13
blueCubes:int  = 14

answer_i:int = 0


#%% Functions
def getGameID(line:str = None) :
    """
    getGameID
    =========
    If the game is possible, then extract its ID

    :param line: The current line of data to check
    :type line: str
    :return: gameID, the current game ID if it is possible
    :rtype: int

    """
    gameID:int = int(line.split(":")[0].split("Game")[-1])
    return gameID

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
    Count all the red cubes in a Game

    :param line: The current line of data to check
    :type line: str
    :return: redOK, a boolean value, if the game is possible or not
    :rtype: bool

    """
    global redOK
    try :
        nbRed:int = int(re.findall('(\d+) red', line)[-1])
    except:
        nbRed:int = 0

    if nbRed > redCubes :
        redOK = False
    else :
        redOK = True

    return redOK

def countGreen(line:str = None):
    """
    countGreen
    ==========
    Count all the green cubes in a Game

    :param line: The current line of data to check
    :type line: str
    :return: greenOK, a boolean value, if the game is possible or not
    :rtype: bool

    """
    global greenOK
    try :
        nbGreen:int = int(re.findall('(\d+) green', line)[-1])
    except:
        nbGreen:int = 0

    if nbGreen > greenCubes :
        greenOK = False
    else :
        greenOK = True

    return greenOK

def countBlue(line:str = None):
    """
    countBlue
    =========
    Count all the blue cubes in a Game

    :param line: The current line of data to check
    :type line: str
    :return: blueOK, a boolean value, if the game is possible or not
    :rtype: bool

    """
    global blueOK
    try :
        nbBlue:int = int(re.findall('(\d+) blue', line)[-1])
    except:
        nbBlue:int = 0

    if nbBlue > blueCubes :
        blueOK = False
    else :
        blueOK = True

    return blueOK

def isGamePossible(gamesList:list = list()):
    """
    isGamePossible
    ==============
    Check all the nb or cubes and compare to their given number
    Get game ID if all the subgames are possible

    :param gamesList: List of the subgames of a game
    :type gamesList: list
    :return: gamePossible, a boolean value if the game is possible or not
    :rtype: bool

    """
    global redOK, greenOK, blueOK, gamePossible
    for game in gamesList:
        redOK = countRed(game)
        greenOK = countGreen(game)
        blueOK = countBlue(game)
        if not redOK or not greenOK or not blueOK:
            gamePossible = False
            return gamePossible
        else :
            gamePossible = True
    return gamePossible

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
    global redOK, greenOK, answer_i
    for line in data:
        gamesList:list = splitGame(line)
        isGamePossible(gamesList)
        if gamePossible:
            gameID = getGameID(line)
            answer_i += gameID
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