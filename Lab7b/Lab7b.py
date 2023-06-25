# Prolog
# Author:  Sophie Nguyen
# Email:  nnguyen177@student.gsu.edu
# Section: 034

import sys
sys.stdin = open('Lab7b/input.txt', 'r')
sys.stdout = open('Lab7b/output.txt', 'w')

file_name = input()     # Enter the input file name
lower_bound = input()   # Enter the lower bound of the search range
upper_bound = input()   # Enter the upper bound of the search range

with open('Lab7b/input1.txt', 'r') as f:
    lines = f.readlines()

for line in lines:
    
    line = line.strip()

    if lower_bound <= line <= upper_bound:
        print(line + " - in range")
    else:
        print(line + " - not in range")
