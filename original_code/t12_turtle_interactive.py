######################################################################
# Author: Scott Heggen      Change this to your name
# Username: heggens         Change this to your username
#
# T12: Events and GUIs
#
# Purpose: To demonstrate how turtle object responds to mouse click events.
# ######################################################################
# Acknowledgements:
#
#   This code is adapted from:
#   http://openbookproject.net/thinkcs/python/english3e/events.html#mouse-events
#   by Dr. Mario Nakazawa
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import turtle


def h1(x, y):
    """
    Event handler for mouse click events

    :param x: x coordinate of the mouse on the screen
    :param y: y coordinate of the mouse on the screen
    :return: None
    """
    tess.goto(x, y)


def main():
    """
    Simple program for demonstrating mouse click events

    :return: None
    """
    global tess
    tess = turtle.Turtle()

    wn = turtle.Screen()
    wn.setup(400,500)
    wn.title("How to handle mouse clicks on the window!")
    wn.bgcolor("lightgreen")

    tess.color("purple")
    tess.pensize(3)
    tess.shape("circle")

    # NOTICE that the screen is responding to the click events!
    wn.onclick(h1)      # Wire up a click handler to the window.

    wn.mainloop()


main()
