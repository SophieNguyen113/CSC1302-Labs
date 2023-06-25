# Prolog
# Author:  Sophie Nguyen
# Email:  nnguyen177@student.gsu.edu
# Section: 034

'''
    Use TKinter to draw a :

        Square - (red color with any size)

        Rectangle - (green border line, with a size of 500,500,100,100)

        Trinagle - (with dashed lines as a border and with any size)
'''

import tkinter as tk

# Create a window.
window = tk.Tk()
window.title('Homework 3')
window.geometry('600x600')

# Create a canvas.
canvas = tk.Canvas(window, width=550, height=550, bg='white')
canvas.pack()

# Draw a red square.
canvas.create_rectangle(10, 10, 100, 100, fill='red')

# Draw a green-bordered rectangle.
canvas.create_rectangle(500, 500, 100, 100, outline='green', width=4)

# Draw a dashed-line triangle.
canvas.create_polygon(300, 200, 400, 400, 200, 400, fill='yellow', outline='black', width=3, dash=(2, 7))

window.mainloop()

