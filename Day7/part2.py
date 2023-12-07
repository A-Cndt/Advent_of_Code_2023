# -*- coding: utf-8 -*-

"""
Day 7: Camel Cards
==================

Part 2
--------
https://adventofcode.com/2023/day/7#part2

Module Info
-----------
:Date: 2023-12-07
:Version: 1.0.0
:Authors: - Alexandre CONDETTE <alexandre.condette@wanadoo.fr>
:platform: Unix, Windows, MacOS
"""

#%% Library
import pathlib

#%% Constants and global Variables
#dayPath:pathlib.Path = pathlib.Path("./Day7")   # Current Path
dayPath:pathlib.Path = pathlib.Path("./Day7")   # Current Path

data:list            = list()   # Input Data
hands:list = list()
bids:list = list()
handsAndBids_l :list = list()
bidsAndRank:list() = list()

runExample:bool = False
answer_i:int = 0
values:str = "AKQJT98765432"

#%% Functions
def handsAndBids(line:str = None):
    """
    """

    global face
    hand, bid = line.split()
    hand = hand.translate(str.maketrans('TJQKA', face))
    best = max(type(hand.replace('0', r)) for r in hand)
    return best, hand, int(bid)

def type(hand):
    """
    """
    return sorted(map(hand.count, hand), reverse=True)

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
    global answer_i, face
    face = 'A0CDE'
    answer_i = sum(rank * bid for rank, (*_, bid) in enumerate(sorted(map(handsAndBids, data)), start=1))
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