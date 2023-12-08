# -*- coding: utf-8 -*-

"""
Day 8: Haunted Wasteland
========================

Part 1
--------
https://adventofcode.com/2023/day/8#part1

Module Info
-----------
:Date: 2023-12-08
:Version: 1.0.0
:Authors: - Alexandre CONDETTE <alexandre.condette@wanadoo.fr>
:platform: Unix, Windows, MacOS
"""

#%% Library
import pathlib
import re
#%% Constants and global Variables
dayPath:pathlib.Path = pathlib.Path("./Day8")   # Current Path
#dayPath:pathlib.Path = pathlib.Path(".")   # Current Path

data:list            = list()   # Input Data
instructions:list = list()

runExample:bool = False

answer_i:int = 0
lineInstructions:int = 0
steps:int = 0

substitution:dict = {'L' : '0', 'R': '1'}
network:dict = dict()

#%% Functions
def getInstructions(data:list = list()):
    """
    """
    global instructions

    instructions=re.findall(r'[\w]', data.split('\n')[0])
    instructions = ''.join(map(lambda x: substitution.get(x, x), instructions))
    return instructions

def getNetwork(data:list =list()):
    """
    """
    global network
    globalNetWork = data.split('\n\n')[-1].split('\n')
    for node in globalNetWork :
        name, connections_str = map(str.strip, node.split("="))
        connections = tuple(map(str.strip, re.findall(r'\w+', connections_str)))
        network[name] = connections

    return network

def analyseNetwork(network:list = list(), instructions:list = list()):
    """
    """

    global lineInstructions, steps

    start = list(network.keys()).index('AAA')
    currentNode = list(network.keys())[start]

    while currentNode != "ZZZ" :
        if lineInstructions >= len(instructions) :
            lineInstructions = 0

        currentNode = network[currentNode][int(instructions[lineInstructions])]

        lineInstructions += 1
        steps += 1

    return steps
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
    getInstructions(data)
    getNetwork(data)
    answer_i = analyseNetwork(network, instructions)
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