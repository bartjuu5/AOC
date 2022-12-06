from copy import copy
import array
import numpy
import matplotlib.pyplot as plt
import os, sys
import parse

file = "input.txt"

file = open(file, 'r')
numbers = file.read().split(",")

fish = [0]*9
for i in numbers:
    fish[int(i)] = fish[int(i)] + 1

for d in range(256):
    tempFish = fish[0]
    for i in range(1,9,1):
        fish[i-1] = fish[i]
    fish[6] += tempFish
    fish[8] = tempFish
print(sum(fish))