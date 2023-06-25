# Prolog
# Author:  Sophie Nguyen
# Email:  nnguyen177@student.gsu.edu
# Section: 034

'''

  Purpose: To read integers user_num and div_num as input
  To output user_num divided by div_num three times using floor divisions. 
    
'''
user_num = int(input()) # Input integer user_num
div_num = int(input())  # Input integer div_num

for x in range(3):                  # 3 times using 'for' loop 
    user_num = user_num//div_num
    print(user_num, end=" ")        # Print the new user_num value 3 times


