from os import path
from tkinter import filedialog
import array
import numpy
import matplotlib.pyplot as plt
import os, sys
import tkinter as tk

filename = "input.txt"

file = open(filename, 'r')
lines = file.readlines()

horz = 0
depth = 0
aim = 0

for i in range(0, len(lines), 1):
    line = lines[i].split(" ")
    if line[0] == "forward":
        horz = horz + int(line[1])
        depth = depth + aim * int(line[1])
    elif line[0] == "down":
        aim = aim + int(line[1])
    elif line[0] == "up":
        aim = aim - int(line[1])
    print(horz, depth, aim)
print(horz*depth)