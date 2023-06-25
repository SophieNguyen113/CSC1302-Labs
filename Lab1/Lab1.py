# Prolog
# Author:  Sophie Nguyen
# Email:  nnguyen177@student.gsu.edu
# Section: 034

'''

  Purpose:
    To read 4 values from input and stores the values in variables 
    first_name,  generic_location, whole_number, and plural_noun.
    The program then uses the input values to output a short story.  

'''

first_name = input()            # Read a value from a user and store the value in first_name
generic_location = input()      # Read a value from a user and store the value in generic_location
whole_number = int(input())     # Read a value from a user and store the value in whole_number
plural_noun = input()           # Read a value from a user and store the value in plural_noun

print(first_name, 'went to', generic_location, 'to buy', whole_number, 'different types of', plural_noun)
# Uses the input values and outputs a story