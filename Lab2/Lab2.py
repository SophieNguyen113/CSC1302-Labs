# Prolog
# Author:  Sophie Nguyen
# Email:  nnguyen177@student.gsu.edu
# Section: 034

'''

  Purpose: Given 3 floating-point numbers x, y, and z
  To output x to the power of z, x to the power of (y to the power of z),
  the absolute value of (x minus y), and the square root of (x to the power of z).

'''

# Import math function from library
import math

x = float(input())  # Input floating number x
y = float(input())  # Input floating number y
z = float(input())  # Input floating number z

value1 = x**z               # x to the power of z
value2 = x**(y**z)          # x to the power of (y to the power of z)
value3 = abs(x-y)           # The absolute value of (x minus y)
value4 = math.sqrt(value1)  # The square root of (x to the power of z)

print(f'{value1:.2f} {value2:.2f} {value3:.2f} {value4:.2f}')
# Print floating-point values with two digits after the decimal point

