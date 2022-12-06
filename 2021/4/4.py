from copy import copy
import array
import numpy
import matplotlib.pyplot as plt
import os, sys

def CheckBingo(board):
    if (board[0]=='-1' and board[1]=='-1' and board[2]=='-1' and board[3]=='-1' and board[4]=='-1') or \
       (board[5]=='-1' and board[6]=='-1' and board[7]=='-1' and board[8]=='-1' and board[9]=='-1') or \
       (board[10]=='-1' and board[11]=='-1' and board[12]=='-1' and board[13]=='-1' and board[14]=='-1') or \
       (board[15]=='-1' and board[16]=='-1' and board[17]=='-1' and board[18]=='-1' and board[19]=='-1') or \
       (board[20]=='-1' and board[21]=='-1' and board[22]=='-1' and board[23]=='-1' and board[24]=='-1') or \
       (board[0]=='-1' and board[5]=='-1' and board[10]=='-1' and board[15]=='-1' and board[20]=='-1') or \
       (board[1]=='-1' and board[6]=='-1' and board[11]=='-1' and board[16]=='-1' and board[21]=='-1') or \
       (board[2]=='-1' and board[7]=='-1' and board[12]=='-1' and board[17]=='-1' and board[22]=='-1') or \
       (board[3]=='-1' and board[8]=='-1' and board[13]=='-1' and board[18]=='-1' and board[23]=='-1') or \
       (board[4]=='-1' and board[9]=='-1' and board[14]=='-1' and board[19]=='-1' and board[24]=='-1'):
        return True
    else:
        return False

filenumbers = "input_numbers.txt"
fileboards = "input_boards.txt"
boardSize = 5

file = open(filenumbers, 'r')
numbers = file.read().split(",")

for n in range(0,len(numbers),1):
    numbers[n] = int(numbers[n])

file = open(fileboards, 'r')
boardLines = file.read().split("\n\n")

boards = []
for n in range(0,len(boardLines),1):
    boards.append(boardLines[n].split())

for b in range(0,len(boards),1):
    for r in range(0,boardSize,1):
        for c in range(0,boardSize,1):
            boards[b][r*boardSize + c] = int(boards[b][r*boardSize + c])

original = copy(boards)
for n in range(0,len(numbers),1):
    tempBoards = copy(boards)
    bingoFound = []
    for b in range(0,len(boards),1):
        for r in range(0,boardSize,1):
            for c in range(0,boardSize,1):
                if tempBoards[b][r*boardSize + c] == numbers[n]:
                    tempBoards[b][r*boardSize + c] = '-1'
        if CheckBingo(tempBoards[b]):
            bingoFound.append(tempBoards[b])
            sum = 0
            for r in range(0,boardSize,1):
                for c in range(0,boardSize,1):
                    if tempBoards[b][r*boardSize + c] != '-1':
                        sum = sum + int(tempBoards[b][r*boardSize + c])
            if len(tempBoards) == 1:
                print(sum*numbers[n])

    if bingoFound != []:
        for b in bingoFound:
            tempBoards.remove(b)
    boards = copy(tempBoards)

