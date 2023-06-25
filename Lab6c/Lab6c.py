# Prolog
# Author:  Sophie Nguyen
# Email:  nnguyen177@student.gsu.edu
# Section: 034

# Below is Python code for input/output
import sys

# For getting input from input.txt file
sys.stdin = open('Lab6c/input.txt', 'r')

# Printing the Output to output.txt file
sys.stdout = open('Lab6c/output.txt', 'w')

def print_num_pattern(num1, num2): 
    if (num1 == -1 or num1 < 0): 
        print(num1, end = ' ') 
        return

    print(num1, end = ' ') 
    print_num_pattern(num1 - num2, num2) 

    print(num1, end = ' ')

if __name__ == "__main__":
    num1 = int(input())
    num2 = int(input())
    print_num_pattern(num1, num2)

    

