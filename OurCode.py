import tkinter as tk
import random
from tkinter import colorchooser, simpledialog, messagebox
#import turtle #commented this out because it creates a whole new screen

class Level1:
    def __init__(self, root):
        '''Initialize the Level1 game with the given Tkinter root.
        Return: None'''
        self.root = root
        self.root.title("Tic_Tac_Toe game")
        self.buttons = []
        self.create_buttons()
        self.available_buttons = []
        self.choose_color_and_symbol()
        self.computer_color()
        self.computer_symbol()
        self.human_score = 0
        self.comp_score = 0
        self.level = 1
        self.display_level()
        self.display_score()
        self.result_label = None
        self.game_over = False

    def display_level(self):
        '''Create or update the level label'''
        if hasattr(self, 'level_text') and self.level_text:
            self.level_text.config(text=f"Level: {self.level}")
        else:
            self.level_text = tk.Label(self.root, text=f"Level: {self.level}", font=("Arial", 8), bg="grey")
            self.level_text.place(x=350, y=0)

    def display_score(self):
        '''this is to display the score, still need to set it up for score change when needed'''
        self.score_label = tk.Label(root, text=self.human_symbol + " score is:" + " " + str(self.human_score) + "  "
        + self.comp_symbol + " " + "score is:" + str(self.comp_score),font=("Arial", 8), bg="white")

        self.score_label.place(x=400, y=0)

    def create_buttons(self):
        '''Create and place the game buttons on the GUI screen.
        Returns: None'''
        for i in range(3):
            row_buttons = []
            for j in range(3):
                # assigning the buttons, defining the grid's dimensions and calling the human_turn method to ensure the user always goes first
                OurGrid = tk.Button(self.root, width=20, height=10, bg="lightgrey", command=lambda row=i, column=j: self.human_turn(row, column))
                OurGrid.grid(row=i, column=j, padx=20, pady=20)
                row_buttons.append(OurGrid)
            self.buttons.append(row_buttons) #adding all created buttons from the grid to our list of buttons

    def human_turn(self, row, column):
        ''' this places the human initial to the screen'''
        self.buttons[row][column]['text'] = self.human_symbol # writing down the symbol on the button
        self.buttons[row][column]['state'] = 'disabled' # disabling the button
        self.buttons[row][column]['bg'] = self.human_color
        if self.check_winner():
            return
        if not self.game_over:
            self.root.after(1000, self.computer_turn)

    def choose_color_and_symbol(self):
        '''this enables the user to choose a color and a symbol'''
        symbol = simpledialog.askstring("Choose Symbol", "Enter your symbol (e.g. X, G.O.A.T, Tom):")
        if symbol:
            self.human_symbol = symbol

        color = colorchooser.askcolor(title="Choose your color")[1]
        if color:
            self.human_color = color

    def computer_color(self):
        '''the computer is randomly picking a color'''
        color_options = ["lightpink", "gold", "salmon", "turquoise", "lightblue", "lightgrey", "lightgreen"]
        color = random.choice(color_options)
        if color:
            self.comp_color = color

    def computer_symbol(self):
        '''the computer is randomly picking a symbol'''
        symbol_options = ["Moana", "Blue", "Error 404", "Player"]
        symbol = random.choice(symbol_options)
        if symbol:
            self.comp_symbol = symbol

    def computer_turn(self):
        '''Execute the computer's move (simple random selection).
        Returns: None'''
        self.available_buttons = [(i, j) for i in range(3) for j in range(3) if self.buttons[i][j]['text'] == ''] # checking which
                                                                        #box is available amongst the total 9 boxes
                                                                        #by checking the boxes that don't have any text in them
        if self.available_buttons:
            row, column = random.choice(self.available_buttons)
            self.buttons[row][column]['text'] = self.comp_symbol #for now we go with the symbol O. we now need to find a way to make it chose random symbol from a list
            self.buttons[row][column]['state'] = 'disabled' #disabling the use of a button twice
            self.buttons[row][column]['bg'] = self.comp_color
            if self.check_winner():
                return

    def check_winner(self):
        '''Checks for a winner by looking at the rows columns and diagonals
         Returns: True if there is a winner, False otherwise.'''
        # Check rows
        for i in range(3):
            if self.buttons[i][0]['text'] == self.buttons[i][1]['text'] == self.buttons[i][2]['text'] and self.buttons[i][0]['text'] != '':
                self.pick_winner(self.buttons[i][0]['text'])
                return True
            # Check Columns
        for j in range(3):
            if self.buttons[0][j]['text'] == self.buttons[1][j]['text'] == self.buttons[2][j]['text'] and self.buttons[0][j]['text']!= '':
                self.pick_winner(self.buttons[0][j]['text'])
                return True
            #Check diagonal
            if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] and self.buttons[0][0]['text'] != '':
                self.pick_winner(self.buttons[0][0]['text'])

            #check other diagonal
            if self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] and \
                    self.buttons[0][2]['text'] != '':
                self.pick_winner(self.buttons[0][2]['text'])
                return True

            'check draw'
            # Check for draw only if no one has won and all buttons are disabled
            if all(self.buttons[i][j]['text'] != '' for i in range(3) for j in range(3)):
                self.check_draw()
                return True
        return False

    def check_draw(self):
        'draw and disable all buttons'
        if not self.game_over:
            self.game_over = True
            self.display_message("It's a draw!")

    def pick_winner(self, winner):
        'picks the winner and disable all buttons'

        if not self.game_over:
            self.game_over = True
            if winner == self.human_symbol:
                self.human_score += 1
            elif winner == self.comp_symbol:
                self.comp_score += 1
            self.display_score()
            self.display_message(f"{winner} wins!")

    def display_message(self, message):
        'Shows the winner'
        if self.result_label:
            self.result_label.destroy()

        self.result_label = tk.Label(self.root, text=message, font=("Arial", 20))
        self.result_label.grid(row=1, column=1, columnspan=1)

        # Ask once after showing the message
        self.root.after(1500, self.reset_game)

    def reset_game(self):
        'Restarts the game for new round '
        if not self.game_over:
            return  # Avoid resetting if the game isn't over

        if self.level == 1:
            choice = messagebox.askyesno("Next Step",
                                         "Would you like to go to Level 2?\nClick 'No' to reset the current level or 'Yes' to go to Level 2.")
            if choice:
                for widget in self.root.winfo_children():
                    widget.destroy()
                game = level2(self.root)
                return

        elif self.level == 2:
            choice = messagebox.askyesno("Next Step",
                                         "Would you like to go to Level 3?\nClick 'No' to reset the current level or 'Yes' to go to Level 3.")
            if choice:
                for widget in self.root.winfo_children():
                    widget.destroy()
                game = Level3(self.root)
                return

        elif self.level == 3:
            # Ask if the player wants to reset to level 1 after reaching level 3
            choice = messagebox.askyesno("Game Over","You have completed Level 3! Would you like to restart the game from Level 1?")
            if choice:
                for widget in self.root.winfo_children():
                    widget.destroy()
                game = Level1(self.root)
                return

        # Just reset the board
        self.game_over = False
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]['text'] = ''
                self.buttons[i][j]['state'] = 'normal'
                self.buttons[i][j]['bg'] = 'lightgrey'

        self.human_score = 0
        self.comp_score = 0
        self.choose_color_and_symbol()
        self.computer_color()
        self.computer_symbol()

        # Update level and score
        self.display_level()

        if self.result_label:
            self.result_label.destroy()
            self.result_label = None


class level2(Level1):
    def __init__(self, root):
        """Initialize the Level2 game with computer trying to block the user win.
        Returns: None"""
        super().__init__(root)
        self.level = 2 # Update level display to Level 2
        self.display_level()


    def computer_turn(self):
        '''with this method, the computer tries to prevent user from winning, but the computer is not trying to win
        this method will be used in our second class for level 1 instead of using the method that ranmly places computer symbol'''

        self.available_buttons = [] #creating a list of available buttons

        #for rows
        for i in range(3):
            if (self.buttons[i][0]['text'] == self.human_symbol and self.buttons[i][1]['text'] == self.human_symbol and self.buttons[i][2]['text'] == ''):
                    self.available_buttons.append((i, 2))
            if (self.buttons[i][1]['text'] == self.human_symbol and self.buttons[i][2][
                'text'] == self.human_symbol and
                    self.buttons[i][0]['text'] == ''):
                self.available_buttons.append((i, 0))
            if (self.buttons[i][0]['text'] == self.human_symbol and self.buttons[i][2][
                'text'] == self.human_symbol and
                self.buttons[i][1]['text'] == ''):
                self.available_buttons.append((i, 1))
        #for columns
        for j in range(3):
            if (self.buttons[0][j]['text'] == self.human_symbol and self.buttons[1][j]['text'] == self.human_symbol and
                    self.buttons[2][j]['text'] == ''):
                self.available_buttons.append((2, j))
            if (self.buttons[0][j]['text'] == self.human_symbol and self.buttons[2][j]['text'] == self.human_symbol and
                     self.buttons[1][j]['text'] == ''):
                self.available_buttons.append((1, j))
            if (self.buttons[1][j]['text'] == self.human_symbol and self.buttons[2][j]['text'] == self.human_symbol and
                    self.buttons[0][j]['text'] == ''):
                self.available_buttons.append((0, j))
        #for diagnals
        if (self.buttons[0][0]['text'] == self.human_symbol and self.buttons[1][1]['text'] == self.human_symbol and
                self.buttons[2][2]['text'] == ''):                self.available_buttons.append((2, 2))
        if (self.buttons[0][0]['text'] == self.human_symbol and self.buttons[2][2]['text'] == self.human_symbol and
                self.buttons[1][1]['text'] == ''):
            self.available_buttons.append((1, 1))
        if (self.buttons[2][2]['text'] == self.human_symbol and self.buttons[1][1]['text'] == self.human_symbol and
                 self.buttons[0][0]['text'] == ''):
               self.available_buttons.append((0, 0))

        if (self.buttons[0][2]['text'] == self.human_symbol and self.buttons[1][1]['text'] == self.human_symbol and
                self.buttons[2][0]['text'] == ''):
            self.available_buttons.append((2, 0))
        if (self.buttons[0][2]['text'] == self.human_symbol and self.buttons[2][0]['text'] == self.human_symbol and
                self.buttons[1][1]['text'] == ''):
            self.available_buttons.append((1, 1))
        if (self.buttons[2][0]['text'] == self.human_symbol and self.buttons[1][1]['text'] == self.human_symbol and
                self.buttons[0][2]['text'] == ''):
            self.available_buttons.append((0, 2))


        if self.available_buttons:
            row, column = random.choice(self.available_buttons)
            self.buttons[row][column]['text'] = self.comp_symbol
            self.buttons[row][column]['state'] = 'disabled'
            self.buttons[row][column]['bg'] = self.comp_color
            return

        # If no blocking move, make a random move
        self.random_move()

    def random_move(self):
        'Random move if no winning or blocking opportunity'
        self.available_buttons = [(i, j) for i in range(3) for j in range(3) if self.buttons[i][j]['text'] == '']
        if self.available_buttons:
            row, column = random.choice(self.available_buttons)
            self.make_move(row, column, self.comp_symbol)

            return

    def make_move(self, row, col, symbol):
        'Make a move for the given symbol'
        self.buttons[row][col]['text'] = symbol
        self.buttons[row][col]['state'] = 'disabled'
        self.buttons[row][col]['bg'] = self.comp_color if symbol == self.comp_symbol else self.human_color
        if self.check_winner():
            return

class Level3(level2):
    def __init__(self, root):
        """Initialize the Level3 game with the computer trying to both block but also win.
        Returns: None"""
        super().__init__(root)
        self.level = 3
        self.display_level()  # Update level display to Level 3

    def computer_turn(self):
        'Computer tries to block the player and win itself'

        #Check if the computer can win
        move = self.find_winning_move(self.comp_symbol)
        if move:
            row, column = move
            self.make_move(row, column, self.comp_symbol)
            return

        # Check if the player is about to win and block it
        move = self.find_winning_move(self.human_symbol)
        if move:
            row, column = move
            self.make_move(row, column, self.comp_symbol)
            return

        #  Random move if no  winning or blocking
        self.random_move()

    def find_winning_move(self, symbol):
        '''Find if there’s a winning move for the given symbol (either computer or player)'''
        for i in range(3):
            # Check rows and columns
            for j in range(3):
                if self.buttons[i][j]['text'] == '' and self.is_winning_move(i, j, symbol):
                    return i, j  # Return the position of the winning move

        # Check diagonals
        for i, j in [(0, 0), (0, 2), (2, 0), (2, 2)]:
            if self.buttons[i][j]['text'] == '' and self.is_winning_move(i, j, symbol):
                return i, j

        return None  # No winning move

    def is_winning_move(self, row, col, symbol):
        '''Check if placing the symbol at (row, col) would result in a win.
        Returns: True if it would result in a win, False otherwise.'''
        original_text = self.buttons[row][col]['text']
        self.buttons[row][col]['text'] = symbol  # Temporarily simulate the move
        is_win = self.is_line_winner(symbol)  # Check if it results in a win
        self.buttons[row][col]['text'] = original_text  # Restore original text
        return is_win

    def make_move(self, row, col, symbol):
        'Make a move for the given symbol'
        self.buttons[row][col]['text'] = symbol
        self.buttons[row][col]['state'] = 'disabled'
        self.buttons[row][col]['bg'] = self.comp_color if symbol == self.comp_symbol else self.human_color
        if self.check_winner():
            return

    def random_move(self):
        '''Random move if no winning or blocking opportunity'''
        self.available_buttons = [(i, j) for i in range(3) for j in range(3) if self.buttons[i][j]['text'] == '']
        if self.available_buttons:
            row, column = random.choice(self.available_buttons)  # Randomly pick a move
            self.make_move(row, column, self.comp_symbol)  # Apply the move
            return

    def is_line_winner(self, symbol):
        '''Checks if the given symbol has a winning line (row, column, or diagonal)'''
        for i in range(3):
            if all(self.buttons[i][j]['text'] == symbol for j in range(3)):  # Check rows
                return True
        for j in range(3):
            if all(self.buttons[i][j]['text'] == symbol for i in range(3)):  # Check columns
                return True
        if all(self.buttons[i][i]['text'] == symbol for i in range(3)):  # Check diagonal (top-left to bottom-right)
            return True
        if all(self.buttons[i][2 - i]['text'] == symbol for i in range(3)):  # Check diagonal (top-right to bottom-left)
            return True
        return False


if __name__ == "__main__":
    root = tk.Tk()

    game = Level1(root)

    root.mainloop()
