# Prolog
# Author:  Sophie Nguyen
# Email:  nnguyen177@student.gsu.edu
# Section: 034

'''

  Purpose:
    Write a for-loop program 
    for all the numbers divisible by 5 
    for the first 100 numbers.   

'''

# Below is Python code for input/output
import sys

# For getting input from input.txt file
sys.stdin = open('Lab3b/input.txt', 'r')

# Printing the Output to output.txt file
sys.stdout = open('Lab3b/output.txt', 'w')

my_list = []
for i in range (1,101):
    if i % 5 == 0:
        my_list.append(i)

print(f'All the numbers divisible by 5 for the first 100 numbers are \n{my_list}')
    
