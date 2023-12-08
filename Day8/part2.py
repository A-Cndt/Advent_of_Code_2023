# -*- coding: utf-8 -*-

"""
Day 8: Haunted Wasteland
========================

Part 2
--------
https://adventofcode.com/2023/day/8#part2

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
dayPath: pathlib.Path = pathlib.Path("./Day8")   # Current Path
#dayPath:pathlib.Path = pathlib.Path(".")   # Current Path

DATA: list = list()   # Input Data

runExample: bool = False

STARTS: list = list()

ANSWER_L: list = list()

substitution: dict = {'L' : '0', 'R': '1'}
NETWORK: dict = dict()

#%% Functions
def get_instructions(data: list) -> str:
    """
    Extracts and processes the instructions from the input data.

    :param data: The input data containing left/right instructions.
    :type data: list
    :return: Processed instructions.
    :rtype: str

    """
    instructions_ = re.findall(r'[\w]', data.split('\n')[0])
    instructions_ = ''.join(map(lambda x: substitution.get(x, x), instructions_))

    return instructions_

def get_network(data: list) -> dict:
    """
    Extracts and processes the network connections from the input data.

    :param data: The input data containing network connections.
    :type data: list
    :return: Processed network connections.
    :rtype: dict
    """

    global_network = data.split('\n\n')[-1].split('\n')

    for node in global_network:
        name, connections_str = map(str.strip, node.split("="))
        connections = tuple(map(str.strip, re.findall(r'\w+', connections_str)))
        NETWORK[name] = connections

    return NETWORK

def analyse_network(network: list, instructions_: list, start: str = str()):
    """
    Analyzes the network based on the left/right instructions starting from a given node.

    :param network: The network connections.
    :type network: dict
    :param instructions: The left/right instructions.
    :type instructions: str
    :param start: The starting node in the network.
    :type start: str
    :return: Number of steps required to reach the 'Z' node.
    :rtype: int

    """

    steps: int = 0
    line_instructions: int = 0
    start_idx: int = list(network.keys()).index(start)
    current_node: list = list(NETWORK.keys())[start_idx]

    while not current_node.endswith('Z'):
        if line_instructions >= len(instructions_):
            line_instructions = 0

        current_node = NETWORK[current_node][int(instructions_[line_instructions])]

        line_instructions += 1
        steps += 1

    return steps

def prime_factors(num: int = 0):
    """
    Decomposes a number into its prime factors.

    :param n: The number to decompose.
    :type n: int
    :return: Dictionary representing the prime factorization of the number.
    :rtype: dict
    """

    factors: dict = dict()
    k: int = 2
    while num != 1:
        exp: int = 0
        while num % k == 0:
            num = num // k
            exp += 1
        if exp != 0:
            factors[k] = exp
        k = k + 1

    return factors

def lcm(num_a, num_b):
    """
    Calculates the least common multiple (LCM) of two numbers using their prime factorizations.

    :param a: The first number.
    :type a: int
    :param b: The second number.
    :type b: int
    :return: The least common multiple of a and b.
    :rtype: int
    """
    factors_a = prime_factors(num_a)
    factors_b = prime_factors(num_b)
    result = 1
    for factor, exponent in factors_a.items():
        if factor in factors_b:
            exp = max(exponent, factors_b[factor])
        else:
            exp = exponent

        result *= factor**exp

    for factor, exponent in factors_b.items():
        if factor not in factors_a:
            result *= factor**exponent

    return result
# %% Answer

def answer():
    """
    answer
    ======

    Solve the current Day part 2

    For this part I decide to compute all the nb of steps for each start points,
    and so the total number of steps is the lcm of each simulation steps

    :param: None
    :return: answer
    :rtype: int

    """

    instructions = get_instructions(DATA)
    get_network(DATA)

    for connection in list(NETWORK.keys()):
        if connection.endswith('A'):
            STARTS.append(connection)

    for start in STARTS:
        ANSWER_L.append(analyse_network(NETWORK, instructions, start))

    answer_i: int = 1

    for ans in ANSWER_L:
        answer_i = lcm(answer_i, ans)

    # answer =
    return answer_i

# %% Output
if __name__ == "__main__":
    if runExample:
        with open(dayPath / 'example.txt', 'r') as raw_data:
            DATA = raw_data.read()
    else:
        with open(dayPath / 'input.txt', 'r') as raw_data:
            DATA = raw_data.read()

    print(answer())
