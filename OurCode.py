import tkinter as tk
import random
from tkinter import colorchooser, simpledialog, messagebox
#import turtle #commented this out because it creates a whole new screen

class Level1:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic_Tac_Toe game")
        self.buttons = []
        self.create_buttons()
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
        '''this is to display the level, still need to set it up for level change when needed'''
        self.level_text = tk.Label(root, text="Level: 1", font=("Arial", 8), bg="grey")
        self.level_text.place(x=350, y=0)

    def display_score(self):
        '''this is to display the score, still need to set it up for score change when needed'''
        self.score_label = tk.Label(root, text=self.human_symbol + " score is:" + " " + str(self.human_score) + "  "
        + self.comp_symbol + " " + "score is:" + str(self.comp_score),font=("Arial", 8), bg="white")

        self.score_label.place(x=400, y=0)

    def create_buttons(self):
        for i in range(3):
            row_buttons = []
            for j in range(3):
                # assigning the buttons, defining the grid's dimensions and calling the human_turn method to ensure the user always goes first
                OurGrid = tk.Button(self.root, width=20, height=10, bg="lightgrey", command=lambda row=i, column=j: self.human_turn(row, column))
                OurGrid.grid(row=i, column=j, padx=20, pady=20)
                row_buttons.append(OurGrid)
            self.buttons.append(row_buttons) #adding all created buttons from the grid to our list of buttons

    def human_turn(self, row, column):
        ''' this draws the human initial to the screen'''
        self.buttons[row][column]['text'] = self.human_symbol # writing down the symbol on the button
        self.buttons[row][column]['state'] = 'disabled' # disabling the button
        self.buttons[row][column]['bg'] = self.human_color
        if self.check_winner():
            return
        if not self.game_over:
            self.root.after(1000, self.computer_turn)

    def max_win_level2(self):
        '''with this method, the computer tries to prevent user from winning and the computer is not trying to win'''
        pass

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
        color_options = ["lightpink", "gold", "salmon", "turquoise", "lightblue", "lightgrey", "lightgreen", "lightorange"]
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

        available_buttons = [(i, j) for i in range(3) for j in range(3) if self.buttons[i][j]['text'] == ''] # checking which
                                                                        #box is available amongst the total 9 boxes
                                                                        #by checking the boxes that don't have any text in them
        if available_buttons:
            row, column = random.choice(available_buttons)
            self.buttons[row][column]['text'] = self.comp_symbol #for now we go with the symbol O. we now need to find a way to make it chose random symbol from a list
            self.buttons[row][column]['state'] = 'disabled' #disabling the use of a button twice
            self.buttons[row][column]['bg'] = self.comp_color
            if self.check_winner():
                return

    def check_winner(self):
        'Checks for a winner by looking at the rows columns and diagonals'
        # Check rows
        for i in range(3):
            if self.buttons[i][0]['text'] == self.buttons[i][1]['text'] == self.buttons[i][2]['text'] and self.buttons[i][0]['text'] != '':
                self.pick_winner(self.buttons[i][0]['text'])
                if "text" ==  self.comp_symbol:
                    self.comp_score += 1
                    self.display_score()
                if "text" ==  self.human_symbol:
                    self.human_score += 1
                    self.display_score()
                return True
            # Check Columns
        for j in range(3):
            if self.buttons[0][j]['text'] == self.buttons[1][j]['text'] == self.buttons[2][j]['text'] and self.buttons[0][j]['text']!= '':
                self.pick_winner(self.buttons[0][j]['text'])
                if "text" ==  self.comp_symbol:
                    self.comp_score += 1
                    self.display_score()
                if "text" ==  self.human_symbol:
                    self.human_score += 1
                    self.display_score()
                return True
            'Check diagonal'
            if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] and self.buttons[0][0]['text'] != '':
                self.pick_winner(self.buttons[0][0]['text'])
            'check other diagonal'
            if self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] and \
                    self.buttons[0][2]['text'] != '':
                self.pick_winner(self.buttons[0][2]['text'])
                if "text" ==  self.comp_symbol:
                    self.comp_score += 1
                    self.display_score()
                if "text" ==  self.human_symbol:
                    self.human_score += 1
                    self.display_score()
                return True
            'check draw'
        if all(self.buttons[i][j]['state'] == 'disabled' for i in range(3) for j in range(3)):
            self.check_draw()
            return True
        return False

    def check_draw(self):
        'draw and disable all buttons'
        self.game_over = True
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]['state'] = 'disabled'  # Disable all buttons
        self.display_message("It's a draw!")

    def pick_winner(self, winner):
        'picks the winner and disable all buttons'
        self.game_over = True
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]['state'] = 'disabled'  # Disable all buttons
        result = f"{winner} wins!"
        self.display_message(result)

    def display_message(self, message):
        'Shows the winner'
        if self.result_label:
            self.result_label.destroy()

        self.result_label = tk.Label(self.root, text=message, font=("Arial", 20))
        self.result_label.grid(row=1, column=1, columnspan=1)  # Display the message in the middle

        self.root.after(1500, self.ask_reset_game)

    def ask_reset_game(self):
        'asks if they want to restart the game'
        self.game_over = False
        result = messagebox.askyesno("Reset Game", "Do you want to reset the game?")
        if result:  # User confirmed
            self.reset_game()

    def reset_game(self):
        'Restarts the game'
        # Reset buttons
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]['text'] = ''
                self.buttons[i][j]['state'] = 'normal'
            self.buttons[i][j]['bg'] = 'lightgrey'

        # Reset scores and level
        self.human_score = 0
        self.comp_score = 0
        self.level = 1

        #resets symbol and color
        self.choose_color_and_symbol()
        self.computer_color()
        self.computer_symbol()

        #update level
        if hasattr(self, 'level_text'):
            self.level_text.destroy()
        self.level_text = tk.Label(self.root, text="Level: 1", font=("Arial", 8), bg="grey")
        self.level_text.place(x=350, y=0)

        #resets score
        if hasattr(self, 'score_label'):
            self.score_label.destroy()
        self.score_label = tk.Label(root, text=self.human_symbol + " score is: " + str(self.human_score) +
                                               "  " + self.comp_symbol + " score is: " + str(self.comp_score),
                                    font=("Arial", 8), bg="white")
        self.score_label.place(x=400, y=0)
        #reset win label
        if self.result_label:
            self.result_label.destroy()
            self.result_label = None
class level2:

    def __init__(self, root):

    def max_win_level1(self):
        '''with this method, the computer tries to prevent user from winning, but the computer is not trying to win
        this method will be used in our second class for level 1 instead of using the method that ranmly places computer symbol'''
        #for the columns
        for i in range(3):
            if self.buttons[i][0][self.human_symbol] == self.buttons[i][1][self.human_symbol] and self.buttons[i][2]['text'] = '':
                pick empty place
            if self.buttons[i][1][self.human_symbol] == self.buttons[i][2][self.human_symbol] and self.buttons[i][0]['text'] = '':
                pick empty place
            if self.buttons[i][0][self.human_symbol] == self.buttons[i][2][self.human_symbol] and self.buttons[i][1]['text'] = '':
                pick empty place
        #for rows
            if self.buttons[0][i][self.human_symbol] == self.buttons[1][i][self.human_symbol] and self.buttons[2][j]['text'] = '':
                pick empty place
            if self.buttons[0][i][self.human_symbol] == self.buttons[2][i][self.human_symbol] and self.buttons[1][j]['text'] = '':
                pick empty place
            if self.buttons[1][i][self.human_symbol] == self.buttons[2][i][self.human_symbol] and self.buttons[0][j]['text'] = '':
                pick empty place
        #for the diagonals
        if self.buttons[0][0][self.human_symbol] == self.buttons[1][1][self.human_symbol] and self.buttons[2][2]['text'] = '':
                pick empty place
        if self.buttons[0][0][self.human_symbol] == self.buttons[2][2][self.human_symbol] and self.buttons[1][1]['text'] = '':
                pick empty place
        if self.buttons[2][2][self.human_symbol] == self.buttons[1][1][self.human_symbol] and self.buttons[0][0]['text'] = '':
                pick empty place
        if self.buttons[0][2][self.human_symbol] == self.buttons[1][1][self.human_symbol] and self.buttons[2][0]['text'] = '':
                pick empty place
        if self.buttons[0][2][self.human_symbol] == self.buttons[2][0][self.human_symbol] and self.buttons[1][1]['text'] = '':
                pick empty place
        if self.buttons[2][0][self.human_symbol] == self.buttons[1][1][self.human_symbol] and self.buttons[0][2]['text'] = '':
                pick empty place




if __name__ == "__main__":
    root = tk.Tk()

    game = Level1(root)

    root.mainloop()
