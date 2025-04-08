######################################################################
# Author: Sara Bako
# Username: bakobagassas
#
# Assignment: HW07: The Game of Nim
#
# Purpose: This program is designed for the game of nim where every player picks a number of items until the basket is
# empty.
#
######################################################################
# Acknowledgements: searched how to pick the minimum number amongst two numbers.
#
####################################################################################
import random

def total_balls():
    ''' this function helps take the initial total number of balls from the user and returns that iniial value to the nim_game function '''
    balls = int(input("please enter the number of total initial balls (min 15)"))
    while balls < 15: #this loop will make the user choose again until the initial total is greater or equal to 15
        balls = int(input("try again! please enter a number that is greater or equal to 15)"))
    return (balls)

def human_pick():
    ''' this function is designed for the user to be able to pick a number between 1 and 4 and will be called from 
    the nim_game function, it returns the number of balls picked by the user to the nim_game function'''
    h_balls = int(input("please enter the number of balls you want to remove(between 1, 2, 3 and 4)")) #asking for no of balls they want to remove
    while h_balls > 4 or h_balls < 1: #looping until they pick a number within the given range
        h_balls = int(input("wrong number! please enter a number that is between 1, 2, 3 and 4)"))
    return (h_balls)

def computer_pick(balls):
    ''' this function is designed for the computer to be able to randomly pick a number between 1 and 4 and will be called from
    the nim_game function, it returns the number of balls picked by the user to the nim_game function'''
    if balls % 5 == 0: #this is in case we have a multiple of 5 we cannot actually win so we just choose randomly
        c_balls = random.randint(1, min(4, balls))
    else:
        c_balls = balls % 5 # this is to make sure we are leaving the user with a multiple of 5 since they can only pick up to 4, it will help the laptop win
    print("the computer picked", c_balls)
    return c_balls


def nim_game():
    ''' this function officially starts the game, calls the other two functions to ask what the user and the computer want to pick
    and also makes the calculation so that we know how many balls remain. This is not a fruitful function'''
    balls = total_balls() #calling the function to ask for initial number of balls
    while balls > 0: #this loops as long as they is still a ball to pick
        # ensuring that we always start with the human user
        h_balls = human_pick() #calling the function to ask for number of balls the user wishes to remove
        balls = int(balls) - int(h_balls) #new total
        if balls == 0 or balls < 0:  #checking is the user wins
            print ("You win! you just picked the last ball/balls")
            return
        print ("there are still", balls, "remaining") #this is in case they don't wim
        print ("now the computer will pick")
        # now it is the computer's turn
        c_balls = computer_pick(balls) #calling the function to ask for number of balls computer wishes to remove
        balls = balls - c_balls  #new total
        if balls == 0 or balls < 0: #this is in case the computer picks the last balls
            print ("Sorry you lost! the computer picked the last ball/balls")
            return
        print ("there are still", balls, "remaining") #this is in case we still have balls remaining

def main():
    ''' this function serves to call the nim_game function where I will call the remaining functions'''
    nim_game() # calling the nim_game function

if __name__ == "__main__":
    main()