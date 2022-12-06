from os import path
from tkinter import filedialog
import array
import numpy
import matplotlib.pyplot as plt
import os, sys
import tkinter as tk

root = tk.Tk()
root.withdraw()
filename = filedialog.askopenfilename()

file = open(filename, 'r')
lines = file.readlines()

incr = 0
sumList = []
for i in range(0, len(lines) - 2, 1):
    sumList.append(int(lines[i]) + int(lines[i + 1]) + int(lines[i + 2]))

for j in range(1, len(sumList), 1):
    if (int(sumList[j]) > int(sumList[j-1])):
        incr = incr + 1
print(incr)