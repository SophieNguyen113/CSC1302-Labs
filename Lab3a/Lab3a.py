# Prolog
# Author:  Sophie Nguyen
# Email:  nnguyen177@student.gsu.edu
# Section: 034

'''

  Purpose:
    Write an if-else conditional statement program 
    to find if a given char is a vowel or not.   

'''

# Below is Python code for input/output
import sys

# For getting input from input.txt file
sys.stdin = open('Lab3a/input.txt', 'r')

# Printing the Output to output.txt file
sys.stdout = open('Lab3a/output.txt', 'w')

char_given = input("Input a letter of the alphabet:")                
# Read a char value from a user and store the value in char_given

vowel_list = ['a','e','i','o','u']      # List of vowels

if char_given in vowel_list:
    print(f' {char_given} is a vowel.')
else: 
    print(f' {char_given} is NOT a vowel, but it is a consonant.')
