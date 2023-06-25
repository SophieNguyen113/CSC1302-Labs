# Prolog
# Author:  Sophie Nguyen
# Email:  nnguyen177@student.gsu.edu
# Section: 034

# Below is Python code for input/output
import sys

# For getting input from input.txt file
sys.stdin = open('Lab6b/input.txt', 'r')

# Printing the Output to output.txt file
sys.stdout = open('Lab6b/output.txt', 'w')

class StudentInfoError(Exception):
    def __init__(self, message):
        self.message = message

def find_ID(name, info):
    if name in info:
        return info[name]
    else:
        raise StudentInfoError("Student ID not found for " + name)

def find_name(ID, info):
    for name, studentID in info.items():
        if studentID == ID:
            return name
    raise StudentInfoError("Student name not found for " + ID)

if __name__ == '__main__':
    student_info = {
        'Reagan' : 'rebradshaw835',
        'Ryley' : 'rbarber894',
        'Peyton' : 'pstott885',
        'Tyrese' : 'tmayo945',
        'Caius' : 'ccharlton329'
    }
    
    user_choice = int(input())
    user_input = input()

    try:
        if user_choice == 0:
            result = find_ID(user_input, student_info)
            print(result)
        elif user_choice == 1:
            result = find_name(user_input, student_info)
            print(result)
        else:
            print("Invalid user choice.")
    except StudentInfoError as e:
        print(e.message)

    
    

