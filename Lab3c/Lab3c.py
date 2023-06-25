# Prolog
# Author:  Sophie Nguyen
# Email:  nnguyen177@student.gsu.edu
# Section: 034

'''

  Purpose:
    The program outputs "In order" if the list is sorted, 
    or "Not in order" if the list is not sorted.   

'''

# Below is Python code for input/output
import sys

# For getting input from input.txt file
sys.stdin = open('Lab3c/input.txt', 'r')

# Printing the Output to output.txt file
sys.stdout = open('Lab3c/output.txt', 'w')



class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]



