from copy import copy
import array
import numpy
import matplotlib.pyplot as plt
import os, sys

filename = "test.txt"

file = open(filename, 'r')
lines = file.read().split("\n")

bitLength = len(lines[0])
numberOfLines = len(lines)

# Part 1
numberOfOnes = [0] * bitLength
for l in range(0, len(lines), 1):
    for b in range(0, bitLength, 1):
        if lines[l][b] == '1':
            numberOfOnes[b] = numberOfOnes[b] + 1

gamma = ""
epsilon = ""
for b in range(0, bitLength, 1):
    if numberOfOnes[b] > (numberOfLines - numberOfOnes[b]):
        gamma = gamma + '1'
        epsilon = epsilon + '0'
    else:
        gamma = gamma + '0'
        epsilon = epsilon + '1'

gammaDec = int(gamma, 2)
epsilonDec = int(epsilon, 2)
print(gammaDec*epsilonDec)

# Part 2
temp = lines
temp2 = lines.copy()
bitPos = 0
while len(temp) > 1:
    numberOfOnes = [0] * len(temp[0])
    for l in temp:
        for i in range(len(l)):
            if(l[i] == '1'):
                numberOfOnes[i] += 1

    mostValue = '0'
    if numberOfOnes[bitPos] >= (len(temp) / 2):
        mostValue = '1'

    for l in temp:
        if(l[bitPos] != mostValue):
            temp2.remove(l)

    bitPos += 1
    temp = temp2.copy()

oxygen = int(temp[0],2)

temp = lines
temp2 = lines.copy()
bitPos = 0
while len(temp) > 1:
    numberOfOnes = [0] * len(temp[0])
    for l in temp:
        for i in range(len(l)):
            if(l[i] == '1'):
                numberOfOnes[i] += 1

    mostValue = '0'
    if numberOfOnes[bitPos] < (len(temp) / 2):
        mostValue = '1'

    for l in temp:
        if(l[bitPos] != mostValue):
            temp2.remove(l)

    bitPos += 1
    temp = temp2.copy()

co2 = int(temp[0],2)

print(oxygen * co2)

