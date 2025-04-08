import tkinter as tk
#import turtle #commented this out because it creates a whole new screen

class GridWidgetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic_Tac_Toe game")
        self.buttons = []
        self.create_buttons()

    def create_buttons(self):
        for i in range(3):
            row_buttons = []
            for j in range(3):
                OurGrid = tk.Button(root, width=20, height=10, command=lambda row=i, column=j: self.draw(row, column))
                OurGrid.grid(row=i, column=j, padx=20, pady=20)
                row_buttons.append(OurGrid)
            self.buttons.append(row_buttons)

    def draw(self, row, column):
        ''' I'm still working on this, it is a method that draws the initials. I am considering splitting it
        in more methods '''
        turn_button = self.buttons[row][column]
        # if computer_turn:
        self.buttons[row][column]['text'] = "O" # searched how to write down a text on the button
        turn_button['state'] = 'disabled' # searched how to disable button
        #if human_turn:

if __name__ == "__main__":
    root = tk.Tk()
    app = GridWidgetApp(root)

    root.mainloop()
