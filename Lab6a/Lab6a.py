# Prolog
# Author:  Sophie Nguyen
# Email:  nnguyen177@student.gsu.edu
# Section: 034

# Below is Python code for input/output
import sys

# For getting input from input.txt file
sys.stdin = open('Lab6a/input.txt', 'r')

# Printing the Output to output.txt file
sys.stdout = open('Lab6a/output.txt', 'w')

def print_all_permutations(nameList, permList=[]):
    if not nameList:
        print(', '.join(permList))
    else:
        for i, name in enumerate(nameList):
            print_all_permutations(nameList[:i] + nameList[i+1:], permList + [name])

if __name__ == "__main__": 
    nameList = input().split(' ')
    print_all_permutations(nameList)

    

