# Prolog
# Author:  Sophie Nguyen
# Email:  nnguyen177@student.gsu.edu
# Section: 034

import sys
sys.stdin = open('Lab7a/input.txt', 'r')
sys.stdout = open('Lab7a/output.txt', 'w')

def draw_triangle(base_length):
    print(' ' * ((20 - base_length) // 2) + '*' * base_length)
    draw_triangle(base_length - 2)
        

if __name__ == '__main__':
    base_length = int(input())
    draw_triangle(base_length)

