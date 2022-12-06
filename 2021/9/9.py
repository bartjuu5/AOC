from collections import deque as queue
from copy import copy
import array
import numpy
import matplotlib.pyplot as plt
import os, sys
import parse

# Direction vectors
dRow = [ -1, 0, 1, 0]
dCol = [ 0, 1, 0, -1]

# Function to check if a cell
# is be visited or not
def isValid(vis, row, col):

    # If cell lies out of bounds
    if (row < 0 or col < 0 or row >= 4 or col >= 4):
        return False

    # If cell is already visited
    if (vis[row][col]):
        return False

    # Otherwise
    return True

# Function to perform the BFS traversal
def BFS(grid, vis, row, col):

    # Stores indices of the matrix cells
    q = queue()

    # Mark the starting cell as visited
    # and push it into the queue
    q.append(( row, col ))
    vis[row][col] = True

    # Iterate while the queue
    # is not empty
    while (len(q) > 0):
        cell = q.popleft()
        x = cell[0]
        y = cell[1]
        print(grid[x][y], end = " ")

        #q.pop()

        # Go to the adjacent cells
        for i in range(4):
            adjx = x + dRow[i]
            adjy = y + dCol[i]
            if (isValid(vis, adjx, adjy)):
                q.append((adjx, adjy))
                vis[adjx][adjy] = True

file = "input.txt"

file = open(file, 'r')
lines = file.read().split("\n")

numCol = len(lines[0])
numRow = len(lines)

grid = [[0 for c in range(numCol)] for r in range(numRow)]

for r in range(numRow):
    line = lines[r]
    for c in range(numCol):
        grid[r][c] = int(line[c])

# Part 1
riskLevel = 0
for r in range(numRow):
    for c in range(numCol):
        found = True
        try:
            if grid[r][c] >= grid[r-1][c] and (r-1) >= 0:
                found = False
        except:
            pass
        try:
            if grid[r][c] >= grid[r][c+1] and (c+1) >= 0:
                found = False
        except:
            pass
        try:
            if grid[r][c] >= grid[r+1][c] and (r+1) >= 0:
                found = False
        except:
            pass
        try:
            if grid[r][c] >= grid[r][c-1] and (c-1) >= 0:
                found = False
        except:
            pass
        if found:
            # Part 2
            vis = [[ False for i in range(numCol)] for i in range(numCol)]
            BFS(grid, vis, r, c)

            print(grid[r][c])
            riskLevel = riskLevel + grid[r][c] + 1
print(riskLevel)












