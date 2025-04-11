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

import unittest




class Label:
    #Label for testing
    def __init__(self, master, text, font):
        self.master = master
        self.text = text
        self.font = font


class Button:
    # buttons for testing.
    def __init__(self, text=''):
        self.text = text
        self.state = 'normal'


class TicTacToe:
    def __init__(self, root, buttons):
        self.root = root
        self.buttons = buttons

    def check_winner(self):
        'checks for a winner by looking at the rows columns and diagonals'
        # Check rows
        for i in range(3):
            if self.buttons[i][0].text == self.buttons[i][1].text == self.buttons[i][2].text and self.buttons[i][0].text != '':
                self.pick_winner(self.buttons[i][0].text)
                return True

        # Check columns
        for j in range(3):
            pass

        return False

    def pick_winner(self, winner):
        'Picks the winner and disables all buttons'
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].state = 'disabled'  # Disable all buttons
        result = f"{winner} wins!"
        self.display_message(result)

    def display_message(self, message):
        'Displays the winner message'
        label = Label(self.root, message, font=("Arial", 20))
        return label


class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        # Create a 3x3 grid of Button objects
        self.buttons = [[Button() for _ in range(3)] for _ in range(3)]
        # Initialize the TicTacToe game
        self.game = TicTacToe(root=None, buttons=self.buttons)

    def test_check_winner_row(self):
        # test a row win with 'X'
        self.buttons[0][0].text = 'X'
        self.buttons[0][1].text = 'X'
        self.buttons[0][2].text = 'X'

        result = self.game.check_winner()
        self.assertTrue(result)
        # Check if the buttons are off
        self.assertEqual(self.buttons[0][0].state, 'disabled')
        self.assertEqual(self.buttons[0][1].state, 'disabled')
        self.assertEqual(self.buttons[0][2].state, 'disabled')


    def test_pick_winner(self):
        # test a winner 'X'
        winner = 'X'

        # Before picking winner, buttons are on
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].state = 'normal'

        # Call pick_winner
        self.game.pick_winner(winner)

        # After picking winner, all buttons should be off
        for i in range(3):
            for j in range(3):
                self.assertEqual(self.buttons[i][j].state, 'disabled')

    def test_display_message(self):
        # Tests if the message is shown correctly
        message = 'X wins!'
        result_label = self.game.display_message(message)
        self.assertEqual(result_label.text, message)
        self.assertEqual(result_label.font, ("Arial", 20))


if __name__ == '__main__':
    unittest.main()

