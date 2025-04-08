######################################################################
# Author: David Wood, Sara Bako
# Username: woodd,bakobagassas
#
# P01 - Final Project
#
# Purpose: To Make a tic tac toe game against the computer
#
#
#######################################################################
####################################################################################
import turtle
import tkinter as tk

def draw_x(center_x, center_y, size):
    """Draws an 'X'  with the given size."""
    half_size = size / 2
    turtle.penup()

    # Line from top-left to bottom-right
    turtle.goto(center_x - half_size, center_y + half_size)
    turtle.pendown()
    turtle.goto(center_x + half_size, center_y - half_size)

    # Line from bottom-left to top-right
    turtle.penup()
    turtle.goto(center_x - half_size, center_y - half_size)
    turtle.pendown()
    turtle.goto(center_x + half_size, center_y + half_size)

    turtle.penup()





def main():
    draw_x(0,2,100)
main()
