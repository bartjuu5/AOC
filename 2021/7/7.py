from copy import copy
import array
import numpy
import matplotlib.pyplot as plt
import os, sys
import parse

file = "input.txt"

file = open(file, 'r')
numbers = file.read().split(",")

count = 0
for n in numbers:
    numbers[count] = int(n)
    count = count + 1

minX = min(numbers)
maxX = max(numbers)

#part 1
minFuel = 1000000000
for i in range(minX,maxX,1):
    totalFuel = 0
    for n in numbers:
        totalFuel = totalFuel + abs(i-n)
    minFuel = min(totalFuel, minFuel)
    if totalFuel > minFuel:
        break

print(minFuel)

#part 2 (n(n+1)/2)
minFuel = 1000000000
for i in range(minX,maxX,1):
    totalFuel = 0
    for n in numbers:
        totalFuel = totalFuel + int((abs(i-n)*(abs(i-n) + 1)) / 2)
    minFuel = min(totalFuel, minFuel)
    if totalFuel > minFuel:
        break

print(minFuel)

