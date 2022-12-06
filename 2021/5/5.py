from copy import copy
import array
import numpy
import matplotlib.pyplot as plt
import os, sys
import parse

file = "input.txt"

file = open(file, 'r')
lines = file.read().split("\n")
fmt = '{},{} -> {},{}'

x1 = []
y1 = []
x2 = []
y2 = []
for l in lines:
    x_1, y_1, x_2, y_2 = parse.parse(fmt, l)
    x1.append(int(x_1))
    y1.append(int(y_1))
    x2.append(int(x_2))
    y2.append(int(y_2))

maxX = max(max(x1), max(x2))
maxY = max(max(y1), max(y2))

grid = [[0 for c in range(maxY + 1)] for r in range(maxX + 1)]

for i in range(0,len(lines),1):
    if x1[i] == x2[i]:
        for y in range(min(y1[i], y2[i]),max(y1[i], y2[i])+1,1):
            grid[y][x1[i]] = grid[y][x1[i]] + 1
    elif y1[i] == y2[i]:
        for x in range(min(x1[i], x2[i]),max(x1[i], x2[i])+1,1):
            grid[y1[i]][x] = grid[y1[i]][x] + 1
    else:
        if x1[i] < x2[i] and y1[i] < y2[i]:
            for j in range(0, abs(x1[i] - x2[i]) + 1,1):
                grid[y1[i] + j][x1[i] + j] = grid[y1[i] + j][x1[i] + j] + 1
        elif x1[i] > x2[i] and y1[i] < y2[i]:
            for j in range(0, abs(x1[i] - x2[i]) + 1,1):
                grid[y1[i] + j][x1[i] - j] = grid[y1[i] + j][x1[i] - j] + 1
        elif x1[i] < x2[i] and y1[i] > y2[i]:
            for j in range(0, abs(x1[i] - x2[i]) + 1,1):
                grid[y1[i] - j][x1[i] + j] = grid[y1[i] - j][x1[i] + j] + 1
        elif x1[i] > x2[i] and y1[i] > y2[i]:
            for j in range(0, abs(x1[i] - x2[i]) + 1,1):
                grid[y1[i] - j][x1[i] - j] = grid[y1[i] - j][x1[i] - j] + 1

total = 0
for i in range(0,maxY + 1,1):
    for j in range(0,maxX + 1,1):
        if grid[i][j] >= 2:
            total = total + 1

print(total)
