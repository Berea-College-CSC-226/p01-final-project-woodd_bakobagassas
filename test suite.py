######################################################################
# Author: Saratou Bako and David Wood
# Username: bakobagassas and woodd
#
# Assignment: P01
#
# Purpose: This program is designed to test for the Tic_Tac_Toe game where every player put their symbol into a
# box intil one of them gets 3 of their symbols aligned either vertically, horizontally or diagonal
#
#
######################################################################
# Acknowledgements:
#
#
####################################################################################
from OurCode import Level1
import sys

from inspect import getframeinfo, stack

def unittest(did_pass):
    """
    Print the result of a unit test.

    :param did_pass: a boolean representing the test
    :return: None
    """

    caller = getframeinfo(stack()[1][0])
    linenum = caller.lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def test_suite():
    'this is to actually test the two fruitful function is_valid_modulo and  is_valid_input'
    # testing the is_valid_input function

    game = Level1
    unittest(check_winner(...) == True) #Testing for correct amount of numbers
    unittest(check_winner(...) == False) # testing for when the number is too little


    # testing the is_valid_modulo function
    unittest(check_draw(...) == True) # testing for correct scanned number
    unittest(check_draw(...) == False) # testing for incorrect scanned number

if __name__ == "__main__":
    test_suite()
