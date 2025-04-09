import tkinter as tk
import random
#import turtle #commented this out because it creates a whole new screen

class Level1:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic_Tac_Toe game")
        self.buttons = []
        self.create_buttons()

    def create_buttons(self):
        for i in range(3):
            row_buttons = []
            for j in range(3):
                # assigning the buttons, defining the grid's dimensions and calling the human_turn method to ensure the user always goes first
                OurGrid = tk.Button(self.root, width=20, height=10, command=lambda row=i, column=j: self.human_turn(row, column))
                OurGrid.grid(row=i, column=j, padx=20, pady=20)
                row_buttons.append(OurGrid)
            self.buttons.append(row_buttons) #adding all created buttons from the grid to our list of buttons

    def human_turn(self, row, column):
        ''' this draws the human initial to the screen'''
        self.buttons[row][column]['text'] = "X" # writing down the symbol on the button
        self.buttons[row][column]['state'] = 'disabled' # disabling the button
        self.root.after(1000, self.computer_turn)  # searched how to delay before calling
        if self.check_winner():
            return

    def max_computer_win(self):
        pass

    def UserSymbolAndColor(self):
        '''search how to change text color, button color and add a user input '''
        pass

    def CompSymbolandColor(self):
        pass

    def computer_turn(self):
        '''for now the computer is randomly placing its symbol, until we write a method that maximizes win'''
        available_buttons = [(i, j) for i in range(3) for j in range(3) if self.buttons[i][j]['text'] == ''] # checking if which
                                                                        #box is available amongst the total 9 boxes
                                                                        #by checking the boxes that don't have any text in them
        if available_buttons:
            row, column = random.choice(available_buttons)
            self.buttons[row][column]['text'] = "O" #for now we go with the symbol O. we now need to find a way to make it chose random symbol from a list
            self.buttons[row][column]['state'] = 'disabled' #disabling the use of a button twice
            if self.check_winner():
                return

    def check_winner(self):
        'Checks for a winner by looking at the rows columns and diagonals'
        # Check rows
        for i in range(3):
            if self.buttons[i][0]['text'] == self.buttons[i][1]['text'] == self.buttons[i][2]['text'] and self.buttons[i][0]['text'] != '':
                self.pick_winner(self.buttons[i][0]['text'])
                return True
            # Check Columns
        for j in range(3):

            pass
        return False

    def pick_winner(self, winner):
        'picks the winner and disable all buttons'
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]['state'] = 'disabled'  # Disable all buttons
        result = f"{winner} wins!"
        self.display_message(result)

    def display_message(self, message):
        'Shows the winner'
        result_label = tk.Label(self.root, text=message, font=("Arial", 20))
        result_label.grid(row=1, column=1, columnspan=1)  # Display the message in the middle


if __name__ == "__main__":
    root = tk.Tk()
    game = Level1(root)

    root.mainloop()
