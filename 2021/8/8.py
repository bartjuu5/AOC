from copy import copy
import array
import numpy
import matplotlib.pyplot as plt
import os, sys
import parse

file = "input.txt"

file = open(file, 'r')
lines = file.read().split("\n")

# Part 1
total = 0
for line in lines:
    parts = line.split('|')
    for numbers in parts[1].split(' '):
        if len(numbers) == 2 or len(numbers) == 3 or len(numbers) == 4 or len(numbers) == 7:
            total = total + 1

print(total)

# Part 2
total = 0
for line in lines:
    parts = line.split('|')
    sets = ['']*10
    subsets = ['']*3

    # 1, 4, 7, 8
    for numbers in parts[0].split(' '):
        if len(numbers) == 2:
            sets[1] = set(numbers)
        elif len(numbers) == 3:
            sets[7] = set(numbers)
        elif len(numbers) == 4:
            sets[4] = set(numbers)
        elif len(numbers) == 7:
            sets[8] = set(numbers)

    # 6, 9
    for numbers in parts[0].split(' '):
        if len(numbers) == 6 and len(set(numbers).difference(sets[4])) == 2:
            sets[9] = set(numbers)
        if len(numbers) == 6 and len(set(numbers).difference(sets[1])) == 5:
            sets[6] = set(numbers)

    # 0
    for numbers in parts[0].split(' '):
        if len(numbers) == 6 and set(numbers) != sets[6] and set(numbers) != sets[9]:
            sets[0] = set(numbers)

    subsets[0] = sets[7].difference(sets[1])
    subsets[1] = sets[8].difference(sets[9])
    subsets[2] = sets[8].difference(sets[6])

    # 5
    sets[5] = sets[9].difference(subsets[2])

    # 2
    for numbers in parts[0].split(' '):
        (bar,) = subsets[1]
        if len(numbers) == 5 and bar in set(numbers):
            sets[2] = set(numbers)

    # 3
    for numbers in parts[0].split(' '):
        if len(numbers) == 5 and set(numbers) != sets[2] and set(numbers) != sets[5]:
            sets[3] = set(numbers)

    # outcome
    numberString = ""
    for toFind in parts[1].split(' '):
        for i in range(0,len(sets),1):
            if sets[i] == set(toFind):
                numberString = numberString + str(i)
                break
    number = int(numberString)
    total = total + number

print(total)