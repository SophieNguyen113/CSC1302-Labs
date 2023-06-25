# Prolog
# Author:  Sophie Nguyen
# Email:  nnguyen177@student.gsu.edu
# Section: 034

'''

  Purpose: To create a list with the lab instructor's values,
  To write methods and then show the outputs

'''

def myMax(list1):           # Find max
 
    max = list1[0]

    for x in list1:
        if x > max:
            max = x
 
    return max

def myMin(list1):           # Find min
 
    min = list1[0]

    for x in list1:
        if x < min:
            min = x
 
    return min

def mySum(list1):           # Find sum
 
    sum = 0

    for x in list1:
        sum += x
 
    return sum

def myLastRemove(list1):         # To remove and return the last item in the list
 
    list1 = list1[ : -1]
 
    return list1
 
list1 = [10,1,30,20,4,9,19,6]

print(myMin(list1))
print(myMax(list1))
print(mySum(list1))
print(myLastRemove(list1))




